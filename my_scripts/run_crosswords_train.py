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

from swarm.environment.domain.crosswords.env import MiniCrosswordsEnv
from swarm.environment.agents.agent_registry import AgentRegistry
from swarm.graph.swarm import Swarm
from swarm.optimizer.edge_optimizer.optimization import optimize
from swarm.environment.domain.crosswords.evaluator import CrosswordsEvaluator


if __name__ == "__main__":

    train_data_file = str(sys.argv[1])
    model_name = sys.argv[2]
    experiment_id = int(sys.argv[3])

    with open(train_data_file, "r") as file:
        test_data = json.load(file)

    # randomness
    torch.manual_seed(experiment_id)
    np.random.seed(experiment_id)
    random.seed(experiment_id)
    print(experiment_id)

    # initialize evaluator, swarm
    init_connection_probability = .1
    epochs = 3
    batch_size = 1
    use_learned_order = True
    include_inner_agent_connections = True
    connect_output_nodes_to_final_node = True
    window_size = int(len(test_data) / batch_size)

    evaluator = CrosswordsEvaluator(
        test_data,
        batch_size=batch_size,
        metric="words",
        window_size=window_size,
    )

    swarm = Swarm(
        ["CrosswordsReflection", "CrosswordsToT"],
        "crosswords",
        model_name,
        final_node_class="ReturnAll",
        final_node_kwargs={},
        edge_optimize=True,
        init_connection_probability=init_connection_probability,
        connect_output_nodes_to_final_node=connect_output_nodes_to_final_node,
        include_inner_agent_connections=include_inner_agent_connections
    )
    print("swarm: ", swarm)

    optimize(swarm,
             evaluator,
             batch_size=batch_size,
             num_iter=int(epochs * len(test_data) / batch_size),
             display_freq=1,
             record=True,
             experiment_id=experiment_id,
             lr=.25,
             use_learned_order=use_learned_order
             )

    time.sleep(5)
