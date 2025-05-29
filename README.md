# dynamic_swarm




## 本地模型起服务

```bash

# 7B 模型
nohup vllm serve ./resources/Qwen/Qwen2___5-7B-Instruct --gpu_memory_utilization 0.9 --max_model_len 5000 > vllm_log_1.log & 


```



## 采用ICL 进行推理

QWEN 7B 模型 下的实验

```bash

# 在已有demo数据的加持下推理
export OPENAI_API_KEY="EMPTY"
export num_reflections=1
export num_inner_iters=2
export depth=5
export branch_factor=2
export num_iters=1
export LM_MODEL_NAME=./resources/Qwen/Qwen2___5-7B-Instruct
export add_direct_cues="false"
export demo_method="retrieved"
export EMBEDDING_MODEL_PATH=./resources/bge-base-en-v1___5
export TOP_K=6

# 采用学习得到的图结构进行推理
nohup python -u my_scripts/run_crosswords_eval_graphs.py graph_45_0 test ./result/crosswords/tmp1 > train_0.log &
0.xxxx
# 

```