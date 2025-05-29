import asyncio
import json
import os
from dataclasses import asdict
from typing import List, Union, Optional
from dotenv import load_dotenv
import random
import async_timeout
from openai import OpenAI, AsyncOpenAI
from tenacity import retry, wait_random_exponential, stop_after_attempt
import time
from typing import Dict, Any

from swarm.utils.log import logger
from swarm.llm.format import Message
from swarm.llm.price import cost_count
from swarm.llm.llm import LLM
from swarm.llm.llm_registry import LLMRegistry


LM_STUDIO_URL = "http://localhost:8000/v1"
lm_model_name = os.getenv(f"LM_MODEL_NAME")


load_dotenv()
OPENAI_API_KEYS=[os.getenv(f"OPENAI_API_KEY")]
for i in range(10):
    if os.getenv(f"OPENAI_API_KEY{i}"):
        OPENAI_API_KEYS.append(os.getenv(f"OPENAI_API_KEY{i}"))

print("OPENAI_API_KEYS: ", OPENAI_API_KEYS)


def gpt_chat(
    model: str,
    messages: List[Message],
    max_tokens: int = 8192,
    temperature: float = 0.0,
    num_comps=1,
    return_cost=False,
) -> Union[List[str], str]:
    if messages[0].content == '$skip$':
        return ''

    api_kwargs: Dict[str, Any]
    if model == "lmstudio" or os.getenv(f"OPENAI_API_KEY") == "EMPTY":
        api_kwargs = dict(api_key="EMPTY", base_url=LM_STUDIO_URL)
    else:
        api_key = random.sample(OPENAI_API_KEYS, 1)[0]
        api_kwargs = dict(api_key=api_key)

    # print("api_kwargs: ", api_kwargs)
    client = OpenAI(**api_kwargs)

    formated_messages = [asdict(message) for message in messages]
    # print("formated_messages: ", formated_messages)

    response = client.chat.completions.create(model=lm_model_name,
    messages=formated_messages,
    max_tokens=max_tokens,
      temperature=0.7,
      top_p=0.9,
    frequency_penalty=1.2,
    presence_penalty=0.0,
    n=num_comps)

    if num_comps == 1:
        cost_count(response, model)
        return response.choices[0].message.content

    cost_count(response, model)

    return [choice.message.content for choice in response.choices]


@retry(wait=wait_random_exponential(max=100), stop=stop_after_attempt(10))
async def gpt_achat(
    model: str,
    messages: List[Message],
    max_tokens: int = 8192,
    temperature: float = 0.0,
    num_comps=1,
    return_cost=False,
) -> Union[List[str], str]:
    if messages[0].content == '$skip$':
        return '' 

    api_kwargs: Dict[str, Any]
    if model == "lmstudio" or os.getenv(f"OPENAI_API_KEY") == "EMPTY":
        api_kwargs = dict(api_key="EMPTY", base_url=LM_STUDIO_URL)
    else:
        api_key = random.sample(OPENAI_API_KEYS, 1)[0]
        api_kwargs = dict(api_key=api_key)
    aclient = AsyncOpenAI(**api_kwargs)

    formated_messages = [asdict(message) for message in messages]
    try:
        async with async_timeout.timeout(1000):
            # print(json.dumps(formated_messages, ensure_ascii=False))
            response = await aclient.chat.completions.create(model=lm_model_name,
            messages=formated_messages,
            max_tokens=max_tokens,
            temperature=0.7,
            top_p=0.9,
            frequency_penalty=1.2,
            presence_penalty=0.0,
            n=num_comps)

    except asyncio.TimeoutError:
        print('Timeout')
        raise TimeoutError("GPT Timeout")
    if num_comps == 1:
        cost_count(response, model)
        return response.choices[0].message.content
    
    cost_count(response, model)

    return [choice.message.content for choice in response.choices]


@LLMRegistry.register('GPTChat')
class GPTChat(LLM):

    def __init__(self, model_name: str):
        self.model_name = model_name

    async def agen(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        num_comps: Optional[int] = None,
        ) -> Union[List[str], str]:

        if max_tokens is None:
            max_tokens = self.DEFAULT_MAX_TOKENS
        if temperature is None:
            temperature = self.DEFAULT_TEMPERATURE
        if num_comps is None:
            num_comps = self.DEFUALT_NUM_COMPLETIONS

        if isinstance(messages, str):
            messages = [Message(role="user", content=messages)]

        # print("\n")
        # print("agen messages: ", len(messages))
        # for msg in messages:
        #     print("msg.role: ", msg.role)
        #     print("msg.content: ", msg.content)
        #     print("\n")
        # print("\n")

        return await gpt_achat(self.model_name,
                               messages,
                               max_tokens,
                               temperature,
                               num_comps)

    def gen(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        num_comps: Optional[int] = None,
        ) -> Union[List[str], str]:

        if max_tokens is None:
            max_tokens = self.DEFAULT_MAX_TOKENS
        if temperature is None:
            temperature = self.DEFAULT_TEMPERATURE
        if num_comps is None:
            num_comps = self.DEFUALT_NUM_COMPLETIONS

        if isinstance(messages, str):
            messages = [Message(role="user", content=messages)]

        return gpt_chat(self.model_name,
                        messages, 
                        max_tokens,
                        temperature,
                        num_comps)
