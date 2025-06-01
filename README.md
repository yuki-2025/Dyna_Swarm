<<<<<<< HEAD
# AgentNet: Towards a Flexible, Graph-Based Multi-Agent System
=======
# dyna_swarm
>>>>>>> 69d9581d95b92e56e8c9a82285d53dfc852b322a

<font size=7><div align='center' > [[📖Paper](https://arxiv.org/pdf/2501.019)] [[🍎 Homepage](https://.github.io/)] </div></font>
 
<p align="center">
    <img src="./asset/banner.png" width="80%" height="80%">
</p>

  
<font size=7><div align='center' >  .🌟 </div></font>  
You can experience our demo here (Coming soon)
 

## Contents <!-- omit in toc -->
 
## 👀 AgentNet Overview 

On 2024.12.12, we launched AgentNet, the first-ever open‐source flexible graph-based multi-agent system that lets researchers and practitioners define, train, and deploy dynamic collaboration graphs without reimplementing core RL or LLM wrappers. Now (2025.05.20), we bring AgentNet v2.0 with a host of new capabilities to make multi-agent reasoning more accessible, efficient, and customizable.

### 🌟 What’s New in AgentNet v2.0?

We are excited to present AgentNet v2.0, which builds on the original release by introducing:

1. **Enhanced Graph Selector Module**: Switched to a more expressive LoRA fine-tuning routine that can now handle up to 20 candidate graph templates per query. This allows AgentNet to learn richer branching strategies and select more nuanced agent interactions based on context.Added support for multi-objective selector losses—users can now jointly optimize for both downstream task performance and computation cost, letting the graph selector balance accuracy vs. latency.

2. **Modular Agent Plug-Ins**: Released a library of pre-built agent components (e.g., “MathSolver,” “TextVerifier,” “CodeSynthesizer”) that can be dropped into any collaboration graph without additional wrapping. Each plug-in comes with standardized input/output schemas, making custom graphs quicker to assemble. Provided a new API endpoint so users can register their own Hugging Face or OpenAI models as AgentNet agents; no need to rewrite core AgentNet code.

3. **A2C Training Pipeline Upgrades** : Improved stability by integrating per-agent value baselines—each agent now maintains its own critic network, reducing variance in the advantage estimates when updating the graph policy. Expanded built-in support for distributed training (Torch DDP and DeepSpeed). Users can train on hundreds of GPUs out of the box, accelerating large-scale graph policy learning from days to hours.**

4. **Visualization & Debugging Tools**: Introduced a real-time graph execution visualizer: as queries flow through the selected graph, users can inspect token-level attention flows and agent activations in a web UI. Added gradient‐tracking mode for graph parameters—now it’s trivial to see how much each edge weight is influencing overall loss, making it easier to debug why certain agent pathways are favored.

5. **Extended Benchmark Suite & Tutorials**: *Coming soon**
Bundled an expanded evaluation suite that includes not only Crossword and Game-of-24, but also MMLU, BBH, and HumanEval. Benchmarks come pre-configured, with sample config files for replicating published results.

Published step-by-step notebooks showing how to:
1. Define a custom multi-agent graph for a reasoning task.
2. Fine-tune the graph selector on a new dataset.
3. Quantize agents for CPU-only inference.

 

## ⭐ Setup
### Requirements and Installation
```
git clone https://github.com/yuki-2025/Dyna_Swarm
cd agentnet
conda create -n agentnet python=3.10 -y
conda activate agentnet
pip install --upgrade pip
pip install -r requirements.txt 
```

### Data Preparation
- First, prepare the npy file for direct cues, used to load the FAISS index
```
python my_scripts/demo_data_collect/construct_direct_cues.py
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/direct_demos.json /root/autodl-tmp/my_gptswarm_icl/resources/bge-base-en-v1___5 my_scripts/demo_data_collect/direct_demos.npy

```

- Prepare the npy files for demos
```
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_propose.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_propose.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_if_correct.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_if_correct.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_suggest.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_suggest.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_value.json /root/autodl-tmp/tot_icl/resources/BAAI/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_value.npy

```

- Run the MAS based on the 72B model (with direct cues) on the training samples to collect demo data
#### Graph structure: result/crosswords/tmp1/graph_8_0.pt
```
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

```


- Process the prompt-response data generated by the large model. Split into four demo sets according to prompt type, all formatted as input-output pairs

---
### Inference Using ICL
#### Experiments with the QWEN 7B Model:

- Prepare demo retrievers for different prompt types. Generate the npy files for demos
```

python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_propose.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_propose.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_if_correct.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_if_correct.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_suggest.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_suggest.npy
python my_scripts/demo_data_collect/encode_data.py my_scripts/demo_data_collect/list_demos_value.json ./resources/bge-base-en-v1___5 my_scripts/demo_data_collect/list_demos_value.npy
```

-  Run inference with the existing demo data
```
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
```

- Use the learned graph structure for inference

```
nohup python -u my_scripts/run_crosswords_eval_graphs.py graph_45_0 test ./result/crosswords/tmp1 > train_0.log &
0.xxxx

```
 
## ✒️ Citation

If you find our work helpful for your research, please consider citing our work.   

```bibtex 
@article{leo2024swarm,
  title={Why Should Next-Gen LLM Multi-Agent Systems Move Beyond Fixed Architectures to Dynamic, Input-Driven Graphs?},
  author={HY. Leong, YQ. Wu},
  journal={arXiv preprint arXiv:2408.052},
  year={2025}
}
```


<<<<<<< HEAD
## &#x1F4E3; Statement

**AgentNet is trained on large-scale open-source corpus, and its output has randomness. Any content generated by AgentNet does not represent the views of the model developers. We are not responsible for any problems arising from the use, misuse, and dissemination of AgentNet, including but not limited to public opinion risks and data security issues.**

 
=======
```
 ## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yuki-2025/Dyna_Swarm&type=Timeline)](https://www.star-history.com/#yuki-2025/Dyna_Swarm&Timeline)
>>>>>>> 69d9581d95b92e56e8c9a82285d53dfc852b322a
