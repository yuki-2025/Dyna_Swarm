

## 本地模型起服务

```bash

# 72B模型
nohup vllm serve /root/autodl-tmp/tot_icl/resources/Qwen/Qwen2___5-72B-Instruct-GPTQ-Int4 --gpu_memory_utilization 0.95 --max_model_len 4800 > vllm_log_1.log & 

# 14B 模型
nohup vllm serve /root/autodl-tmp/my_gptswarm_icl/resources/Qwen2___5-14B-Instruct --gpu_memory_utilization 0.95 --max_model_len 4800 > vllm_log_1.log & 

# 0.5B 模型
nohup vllm serve /root/autodl-tmp/my_gptswarm_icl/resources/Qwen2___5-0___5B-Instruct-GPTQ-Int4 --gpu_memory_utilization 0.9 --max_model_len 4800 > vllm_log_1.log & 


# 7B 模型
nohup vllm serve /root/autodl-tmp/my_gptswarm_icl/resources/Qwen/Qwen2___5-7B-Instruct --gpu_memory_utilization 0.9 --max_model_len 5000 > vllm_log_1.log & 



# Meta-Llama-3___1-8B-Instruct
nohup vllm serve /root/autodl-tmp/ShapLoRA/resources/LLM-Research/Meta-Llama-3___1-8B-Instruct --gpu_memory_utilization 0.90 --max_model_len 7000 > vllm_log_1.log & 



```


## 数据收集


```bash

# 先准备好direct cues的npy文件，用于加载faiss index
python my_scripts/demo_data_collect/构造直接的cues.py
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/direct_demos.json /root/autodl-tmp/my_gptswarm_icl/resources/bge-base-en-v1___5 my_scripts/demo_data_collect/direct_demos.npy

# 准备好demos的npy文件
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_propose.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_propose.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_if_correct.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_if_correct.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_suggest.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_suggest.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_value.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_value.npy



# 在train样本上运行72B模型为基础的MAS（有direct cues），用于收集demo数据
# 图结构：result/crosswords/tmp1/graph_8_0.pt
export OPENAI_API_KEY="EMPTY"
export num_reflections=2
export num_inner_iters=2
export depth=4
export branch_factor=2
export num_iters=1
export LM_MODEL_NAME=/root/autodl-tmp/tot_icl/resources/Qwen/Qwen2___5-72B-Instruct-GPTQ-Int4
export add_direct_cues="true"
export demo_method="fixed"
export EMBEDDING_MODEL_PATH="/root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5"
export TOP_K=6
nohup python -u my_scripts/run_crosswords_eval_graphs.py graph_0_0 train ./result/crosswords/tmp1 > train_0.log &

# python -u my_scripts/run_crosswords_train.py datasets/crosswords/train.json /root/autodl-tmp/tot_icl/resources/Qwen/Qwen2___5-72B-Instruct-GPTQ-Int4 100 


# 处理大模型跑出来的prompt-response数据
# 按照prompt的类型划分为4个demo集合，统一格式为：input-output pair
python my_scripts/demo_data_collect/collect_demo_data.py



```


## 采用ICL 进行推理

QWEN 1.5B 模型 下的实验

```bash

# 准备各类prompt下的demo retriever
# 准备好demos的npy文件
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_propose.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_propose.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_if_correct.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_if_correct.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_suggest.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_suggest.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_value.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_value.npy


# 部署LLM
# QWEN 1.5B 模型
nohup vllm serve /root/autodl-tmp/my_gptswarm_icl_2/resources/Qwen2___5-1___5B-Instruct --gpu_memory_utilization 0.9 --max_model_len 8000 > vllm_log_1.log & 


# 在已有demo数据的加持下推理
export OPENAI_API_KEY="EMPTY"
export num_reflections=1
export num_inner_iters=2
export depth=5
export branch_factor=2
export num_iters=1
export LM_MODEL_NAME=/root/autodl-tmp/my_gptswarm_icl_2/resources/Qwen2___5-1___5B-Instruct
export add_direct_cues="false"
export demo_method="retrieved"
export EMBEDDING_MODEL_PATH=/root/autodl-tmp/my_gptswarm_icl_2/resources/bge-base-en-v1___5
export TOP_K=6

# 采用学习得到的图结构进行推理
nohup python -u my_scripts/run_crosswords_eval_graphs.py graph_45_0 test ./result/crosswords/tmp1 > train_0.log &
0.06666666666666667
# 

```



QWEN 3B 模型 下的实验


```bash

# 准备各类prompt下的demo retriever
# 准备好demos的npy文件
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_propose.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_propose.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_if_correct.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_if_correct.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_suggest.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_suggest.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_value.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_value.npy


# 部署LLM
# QWEN 3B 模型
nohup vllm serve /root/autodl-tmp/my_gptswarm_icl_2/resources/Qwen2___5-3B-Instruct --gpu_memory_utilization 0.9 --max_model_len 8000 > vllm_log_1.log & 


# 在已有demo数据的加持下推理
export OPENAI_API_KEY="EMPTY"
export num_reflections=2
export num_inner_iters=2
export depth=4
export branch_factor=2
export num_iters=1
export LM_MODEL_NAME=/root/autodl-tmp/my_gptswarm_icl/resources/Qwen2___5-3B-Instruct
export add_direct_cues="false"
export demo_method="retrieved"
export EMBEDDING_MODEL_PATH=/root/autodl-tmp/my_gptswarm_icl_2/resources/bge-base-en-v1___5
export TOP_K=6

# 采用 fixed 学习得到的图结构进行推理
nohup python -u my_scripts/run_crosswords_eval_graphs.py graph_100_0 test ./result/crosswords/tmp1 > train_0.log &

avg. utility = 0.228
utilities:  [0.4, 0.2, 0.1, 0.2, 0.3, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.2, 0.1, 0.3, 0.2, 0.3, 0.1, 0.3, 0.3, 0.4, 0.2, 0.3, 0.3, 0.2, 0.3]

# 在retrieved demo下，学习图结构？
xxx

```


QWEN 7B 模型 下的实验

```bash

# 准备各类prompt下的demo retriever
# 准备好demos的npy文件
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_propose.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_propose.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_if_correct.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_if_correct.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_suggest.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_suggest.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_value.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_value.npy


# 在已有demo数据的加持下推理
export OPENAI_API_KEY="EMPTY"
export num_reflections=1
export num_inner_iters=2
export depth=5
export branch_factor=2
export num_iters=1
export LM_MODEL_NAME=/root/autodl-tmp/my_gptswarm_icl/resources/Qwen/Qwen2___5-7B-Instruct
export add_direct_cues="false"
export demo_method="retrieved"
export EMBEDDING_MODEL_PATH=/root/autodl-tmp/my_gptswarm_icl/resources/bge-base-en-v1___5
export TOP_K=6

# 采用学习得到的图结构进行推理
nohup python -u my_scripts/run_crosswords_eval_graphs.py graph_45_0 test ./result/crosswords/tmp1 > train_0.log &
0.xxxx
# 

```