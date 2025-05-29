import copy
import json
import os

import random

from sentence_transformers import SentenceTransformer

from my_scripts.demo_data_collect.existing_demos import list_propose_demos, list_if_correct_demos, list_suggest_demos, \
    list_value_demos
from my_scripts.io_utils import load_json
from my_scripts.logger_utils import LOG
from swarm.graph import Node
from swarm.llm.format import Message

embedding_model_path = os.environ["EMBEDDING_MODEL_PATH"]

from my_scripts.demo_data_collect.retrievers import FaissRetriever

embed_model = SentenceTransformer(
            embedding_model_path
        ).to("cuda")
embed_model.eval()

demo_retriever = FaissRetriever(
    "my_scripts/demo_data_collect/direct_demos.json",
    "my_scripts/demo_data_collect/direct_demos.npy",
    embed_model=embed_model
)

# retriever for demos
propose_demo_retriever = FaissRetriever(
    "my_scripts/demo_data_collect/list_demos_propose.json",
    "my_scripts/demo_data_collect/list_demos_propose.npy",
    embed_model=embed_model
)
if_correct_demo_retriever = FaissRetriever(
    "my_scripts/demo_data_collect/list_demos_if_correct.json",
    "my_scripts/demo_data_collect/list_demos_if_correct.npy",
    embed_model=embed_model
)
suggest_demo_retriever = FaissRetriever(
    "my_scripts/demo_data_collect/list_demos_suggest.json",
    "my_scripts/demo_data_collect/list_demos_suggest.npy",
    embed_model=embed_model
)
value_demo_retriever = FaissRetriever(
    "my_scripts/demo_data_collect/list_demos_value.json",
    "my_scripts/demo_data_collect/list_demos_value.npy",
    embed_model=embed_model
)


def prompt_type_cls(prompt):

    if "list all possible answers for unfilled or changed words" in prompt:
        prompt_type = "propose"
    elif "Respond only Yes or No" in prompt:
        prompt_type = "if_correct"
    elif "Write a plan for the next time." in prompt:
        prompt_type = "suggest"
    elif "Evaluate if there exists a five letter word of some meaning that fit some letter constraints" in prompt:
        prompt_type = "value"
    else:
        raise ValueError("Invalid prompt")

    return prompt_type


class CrosswordsOperation(Node):
    async def llm_query_with_cache(self, prompt):
        cache = self.memory.query_by_id("cache")
        if len(cache) == 0:
            cache = {}
            self.memory.add("cache", cache)
        else:
            cache = cache[0]

        # print("cache: ", len(cache))
        # print("cache: ", cache[0])
        # print("cache: ", cache.keys())
        # cache_tmp = {}
        # if os.path.exists("llm_query_caches.json"):
        #     cache_tmp = load_json(
        #         "llm_query_caches.json"
        #     )
        # cache_tmp.update(cache)
        # with open("llm_query_caches.json", "w", encoding="utf-8") as f:
        #     json.dump(
        #         cache_tmp,
        #         f,
        #         ensure_ascii=True,
        #         indent=2
        #     )

        prompt_0 = copy.copy(prompt)
        response_ = None
        if not prompt in cache:

            prompt_1 = copy.copy(prompt)
            if os.environ["add_direct_cues"] == "true":
                # 在prompt中添加 direct cues, 帮助提升效果
                if "<current query>" in prompt:
                    search_input = prompt.split("<current query>")[1].strip()
                else:
                    search_input = prompt
                retrieved_demos = demo_retriever.search_once(
                    search_input, top_k=18
                )["query2query"]
                random.shuffle(retrieved_demos)
                retrieved_demos = retrieved_demos[:10]

                cue_str = "<cue>\n"
                for r_d in retrieved_demos:
                    # print("r_d: ", r_d)
                    input_ = r_d["sample"]["input"]
                    cue_str += f"{input_}\n\n"
                cue_str += "</cue>\n\n"
                prompt_1 = cue_str + prompt

            prompt_type = prompt_type_cls(prompt_1)
            top_k = int(os.environ["TOP_K"])
            if os.environ["demo_method"] == "fixed":

                if prompt_type == "propose":
                    demos_tmp = copy.deepcopy(list_propose_demos[ :top_k])
                elif prompt_type == "if_correct":
                    demos_tmp = copy.deepcopy(list_if_correct_demos[ :top_k])
                elif prompt_type == "suggest":
                    demos_tmp = copy.deepcopy(list_suggest_demos[ :top_k])
                elif prompt_type == "value":
                    demos_tmp = copy.deepcopy(list_value_demos[ :top_k])
                else:
                    raise ValueError("Invalid prompt_type")

                demo_str = ""
                for r_d in demos_tmp:
                    # print("r_d: ", r_d)
                    input_ = r_d["input"]
                    output_ = r_d["output"]
                    demo_str += f"{input_}\n{output_}\n\n"

            elif os.environ["demo_method"] == "retrieved":
                if "<current query>" in prompt:
                    search_input = prompt.split("<current query>")[1].strip()
                else:
                    search_input = prompt

                if prompt_type == "propose":
                    demos_tmp = propose_demo_retriever.search_once(
                        search_input, top_k=top_k
                    )["query2query"]
                elif prompt_type == "if_correct":
                    demos_tmp = if_correct_demo_retriever.search_once(
                        search_input, top_k=top_k
                    )["query2query"]
                elif prompt_type == "suggest":
                    demos_tmp = suggest_demo_retriever.search_once(
                        search_input, top_k=top_k
                    )["query2query"]
                elif prompt_type == "value":
                    demos_tmp = value_demo_retriever.search_once(
                        search_input, top_k=top_k
                    )["query2query"]
                else:
                    raise ValueError("Invalid prompt_type")

                demo_str = ""
                for r_d in demos_tmp:
                    # print("r_d: ", r_d)
                    input_ = r_d["sample"]["input"]
                    output_ = r_d["sample"]["output"]
                    demo_str += f"{input_}\n{output_}\n\n"

            else:
                raise ValueError("Invalid demo_method")

            prompt_2 = prompt_1.replace(
                "<placeholder>", demo_str
            )
            # print("prompt: ", prompt)

            response_ = await self.llm.agen([Message(role="user", content=prompt_2)], temperature=0.0)
            # prompt_ = prompt.split("</cue>")[1].strip()

            cache[prompt_0] = response_

            # if prompt_type in ["if_correct", "value"]:
            #     cache[prompt_0] = response_
            # else:
            #     cache[prompt_2.split("</cue>")[1].strip()] = response_

            LOG.info(f'prompt_message: {json.dumps({"input": prompt_2, "output": response_}, ensure_ascii=False)}')

        else:
            response_ = cache[prompt_0]
        return response_