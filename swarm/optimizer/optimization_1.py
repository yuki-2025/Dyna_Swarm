import json
import os
import time

import torch
import torch.nn as nn
from tqdm import tqdm
import asyncio
import pickle
import numpy as np

from swarm.graph import GPTSwarmVis


def optimize(swarm,
             evaluator,
             num_iter=100,
             lr=1e-1,
             display_freq=10,
             batch_size=1,
             record=False,
             experiment_id='experiment',
             use_learned_order=False,
             ):
    optimizer = torch.optim.Adam(swarm.connection_dist.parameters(), lr=lr)
    pbar = tqdm(range(num_iter))
    utilities = []
    loop = asyncio.get_event_loop()

    # best_utility = -0.1
    for step in pbar:
        evaluator.reset()
        optimizer.zero_grad()
        tasks = []
        log_probs = []

        model_name = os.getenv(f"LM_MODEL_NAME").split("/")[-1]

        os.makedirs("./result/crosswords/", exist_ok=True)
        os.makedirs(f"./result/crosswords/exp_{model_name}_{experiment_id}/", exist_ok=True)

        results = []
        for i in range(batch_size):
            _graph, log_prob = swarm.connection_dist.realize(
                swarm.composite_graph,
                use_learned_order=use_learned_order
            )
            print("_graph.num_edges: ", _graph.num_edges)
            # 画图
            GPTSwarmVis(
                _graph, style="pyvis", dry_run=False,
                file_name=f"./result/crosswords/exp_{model_name}_{experiment_id}/graph_{step}_{i}.html"
            )

            torch.save(
                _graph,
                f"./result/crosswords/exp_{model_name}_{experiment_id}/graph_{step}_{i}.pt"
            )

            results.append(evaluator.evaluate(_graph, return_moving_average=True))
            log_probs.append(log_prob)

        # time.sleep(3)
        utilities.extend([result[0] for result in results])
        print("utilities: ", utilities)

        if step == 0:
            moving_averages = np.array([np.mean(utilities) for _ in range(batch_size)])
        else:
            moving_averages = np.array([result[1] for result in results])
        loss = (-torch.stack(log_probs) * torch.tensor(np.array(utilities[-batch_size:]) - moving_averages)).mean()
        loss.backward()
        optimizer.step()

        if step % display_freq == display_freq - 1:
            print(
                f'avg. utility = {np.mean(utilities[-batch_size:]):.3f} with std {np.std(utilities[-batch_size:]):.3f}')

            with open(f"result/crosswords/exp_{model_name}_{experiment_id}/utilities_{step}.pkl", "wb") as file:
                pickle.dump(utilities, file),

            torch.save(
                swarm.connection_dist.state_dict(),
                f"result/crosswords/exp_{model_name}_{experiment_id}/edge_logits_{step}.pt"
            )

            with open(f"result/crosswords/exp_{model_name}_{experiment_id}/utilities_{step}.json", "w", encoding="utf-8") as file:
                print("utilities: ", utilities)
                json.dump(
                    utilities,
                    file
                )