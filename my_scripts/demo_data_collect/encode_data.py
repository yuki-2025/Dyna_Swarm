# -*- coding: utf-8 -*-
"""
@Copyright: 2024 Dr Zhu.
@License：the Apache License, Version 2.0
@Author：Dr Zhu, wechat: 15000361164
@version：
@Date：
@Desc: build faiss index for lvlm tasks
"""

import sys

import numpy as np
from tqdm import tqdm

sys.path.append("./")

from my_scripts.demo_data_collect.embed_model import EmbedModel
from my_scripts.io_utils import dump_npy, load_jsonl


def encode_sample_list(list_samples, embed_model=None, batch_size=32):
    tmp_queries = []
    count = 0
    all_text_vectors = []
    for samp in tqdm(list_samples):
        tmp_queries.append(samp["input"])
        count += 1

        if len(tmp_queries) == batch_size:
            text_embeds = embed_model.encode_batch_pairs(
                tmp_queries,
            )
            text_embeds = text_embeds.tolist()
            all_text_vectors.extend(text_embeds)

            tmp_queries = []

    if len(tmp_queries) > 0:
        text_embeds = embed_model.encode_batch_pairs(
                tmp_queries,
            )
        text_embeds = text_embeds.tolist()
        all_text_vectors.extend(text_embeds)

    return all_text_vectors



def encode_corpus(data_path,
                 model_name_or_path=None,
                to_path=None,
                  batch_size=32):

    list_samples = load_jsonl(
        data_path
    )

    embed_model = EmbedModel(
        model_name_or_path
    )

    all_text_vectors = encode_sample_list(list_samples, embed_model=embed_model, batch_size=batch_size)
    all_text_vectors = np.array(all_text_vectors)
    print("all_text_vectors: ", all_text_vectors.shape)

    # all_queries, all_image_paths
    dump_npy(
        all_text_vectors,
        to_path,
    )


if __name__ == "__main__":
    data_path = sys.argv[1]
    model_name_or_path = sys.argv[2]
    to_path = sys.argv[3]

    encode_corpus(data_path,
                  model_name_or_path=model_name_or_path,
                  to_path=to_path,
                  batch_size=32)

