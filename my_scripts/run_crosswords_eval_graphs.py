import json
import os
import time

from tqdm import tqdm
import asyncio
import numpy as np
from copy import deepcopy
import pickle
import torch
import sys
import random

sys.path.append("./")

# from swarm.environment.domain.crosswords.env import MiniCrosswordsEnv
# from swarm.environment.agents.agent_registry import AgentRegistry
# from swarm.graph.swarm import Swarm
# from swarm.optimizer.edge_optimizer.optimization import optimize
from swarm.environment.domain.crosswords.evaluator import CrosswordsEvaluator


def batched_evaluator(evaluator, batch_size, graph, loop):
    tasks = []
    for _ in range(batch_size):
        tasks.append(evaluator.evaluate(deepcopy(graph)))
    return loop.run_until_complete(asyncio.gather(*tasks))


if __name__ == "__main__":

    graph_paths = str(sys.argv[1])
    data_subset = str(sys.argv[2])
    to_folder = str(sys.argv[3])

    data_path = f"datasets/crosswords/{data_subset}.json"
    with open(data_path, "r") as file:
        test_data = json.load(file)

    print("test_data: ", len(test_data))
    time.sleep(3)

    init_connection_probability = .1
    epochs = 1
    batch_size = 1
    use_learned_order = True
    num_batches = int(len(test_data) / batch_size)

    # 初始化evaluator
    evaluator = CrosswordsEvaluator(
        test_data,
        batch_size=batch_size,
        metric="words",
        window_size=num_batches
    )

    graph_paths = graph_paths.split(",")
    loop = asyncio.get_event_loop()
    for g_idx, g_name in enumerate(graph_paths):
        # g_name= g_path.split("/")[-1].replace(".pt", "")
        g_path = os.path.join(to_folder, f"{g_name}.pt")

        graph = torch.load(
            g_path
        )
        print(graph)
        print(f"{graph.num_edges} edges")

        utilities = []
        evaluator.reset()
        for k in range(num_batches):
            # if k == 0:
            #     continue

            utilities += batched_evaluator(evaluator, batch_size, graph, loop)
            print(f"avg. utility = {np.mean(utilities):.3f}")
            time.sleep(5)

            with open(f"./{to_folder}/run_{g_name}_{data_subset}_utilities.json", "w", encoding="utf-8") as file:
                print("utilities: ", utilities)
                json.dump(
                    {
                        "utilities": utilities,
                        "avg_utility": sum(utilities) / len(utilities),
                    },
                    file,
                    ensure_ascii=False,
                    indent=2
                )






