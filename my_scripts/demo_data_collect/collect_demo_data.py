import json
import os
import sys
sys.path.append("./")


from my_scripts.io_utils import load_json, dump_jsonl


list_files = []
for root, dirs, files in os.walk("./my_scripts/demo_data_collect/"):
    for f in files:
        if f.endswith(".log"):
            list_files.append(
                os.path.join(root, f)
            )

list_demos_propose = []
list_demos_if_correct = []
list_demos_suggest = []
list_demos_value = []
seen_inputs = set()
for file_name in list_files:
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if "prompt_message: " in line:
                line = line.split("prompt_message: ")[1]
                samp = json.loads(line)
                input_ = samp["input"]
                output_ = samp["output"]

                assert "</cue>" in input_
                input_ = input_.split("</cue>")[1]

                if "list all possible answers for unfilled or changed words" in input_:
                    prompt_type = "propose"
                elif "Respond only Yes or No" in input_:
                    prompt_type = "if_correct"
                elif "Write a plan for the next time." in input_:
                    prompt_type = "suggest"
                elif "Evaluate if there exists a five letter word of some meaning that fit some letter constraints" in input_:
                    prompt_type = "value"
                else:
                    raise ValueError("Invalid prompt")

                if prompt_type == "propose":
                    assert "<current query>" in input_
                    input_ = input_.split("<current query>")[1].split("Instruct: ")[0]
                    # print("input_: ", input_)
                    # print("*" * 10)
                    input_ = input_.strip() + "\n\n"
                    output_ = output_.strip()
                    # print("output_: ", output_)
                    # print("*" * 10)
                    if input_ in seen_inputs:
                        continue

                    list_demos_propose.append(
                        {
                            "input": input_,
                            "output": output_,
                        }
                    )

                elif prompt_type == "if_correct":
                    print("input_: ", input_)
                    input_ = input_.split("<current query>")[1].strip()
                    output_ = output_.strip()
                    print("input_: ", input_)
                    print("*" * 10)
                    # print("output_: ", output_)

                    if input_ in seen_inputs:
                        continue
                    list_demos_if_correct.append(
                        {
                            "input": input_,
                            "output": output_,
                        }
                    )


                elif prompt_type == "suggest":

                    input_ = input_.split("<current query>")[1].strip()
                    output_ = output_.strip()
                    # print("input_: ", input_)
                    # print("output_: ", output_)
                    # print("*" * 10)

                    if input_ in seen_inputs:
                        continue
                    list_demos_suggest.append(
                        {
                            "input": input_,
                            "output": output_,
                        }
                    )

                elif prompt_type == "value":
                    input_ = input_.split("<current query>")[1]
                    output_ = output_.strip()

                    # print("input_: ", input_)
                    # print("output_: ", output_)
                    # print("*" * 10)

                    if input_ in seen_inputs:
                        continue
                    list_demos_value.append(
                        {
                            "input": input_,
                            "output": output_,
                        }
                    )

                else:
                    raise ValueError("Invalid prompt")

                seen_inputs.add(input_)

dump_jsonl(
    list_demos_propose,
    "my_scripts/demo_data_collect/list_demos_propose.json"
)
dump_jsonl(
    list_demos_if_correct,
    "my_scripts/demo_data_collect/list_demos_if_correct.json"
)
dump_jsonl(
    list_demos_suggest,
    "my_scripts/demo_data_collect/list_demos_suggest.json"
)
dump_jsonl(
    list_demos_value,
    "my_scripts/demo_data_collect/list_demos_value.json"
)

