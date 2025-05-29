import torch
from modelscope import snapshot_download

# model_dir = snapshot_download(
#     "modelscope/Llama-2-7b-chat-ms", revision='v1.0.5',
#     ignore_file_pattern=[r'.+\.bin$'],
#     # ignore_file_pattern=[r'*bin'],
#     cache_dir="./resources/Llama-2-7b-chat-hf"
# )


model_dir = snapshot_download(
    # "modelscope/Llama-2-7b-chat-ms",
    # "modelscope/Llama-2-13b-chat-ms",
    # "AI-ModelScope/Mistral-7B-Instruct-v0.2",
    # "qwen/Qwen1.5-14B-Chat-GPTQ-Int4",
    # "Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4",
    # "Qwen/Qwen2.5-3B-Instruct",
    "Qwen/Qwen2.5-7B-Instruct-GPTQ-Int4",
    # "LLM-Research/Llama-3.2-3B-Instruct",
    # "qwen/Qwen2-7B-Instruct",
    # "Qwen/Qwen2.5-3B-Instruct",
    # "Qwen/Qwen2.5-3B-Instruct-GPTQ-Int4",
    # "LLM-Research/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4",
    # "Qwen/Qwen2.5-7B-Instruct",
    # "qwen/Qwen1.5-14B-Chat",
    # "modelscope/Llama-2-7b-ms",
    # "qwen/Qwen1.5-7B-Chat",
    # "qwen/Qwen1.5-7B",
    # revision='v1.0.2',
    # ignore_file_pattern=[r'.+\.bin$'],
    # ignore_file_pattern=[r'*bin'],
    cache_dir="./resources/"
)

# nohup python -u my_gptswarm/model_download.py > dl_0.log &