import json
import os

from tqdm import tqdm

import numpy as np

def load_json(path_):
    with open(path_, "r", encoding="utf-8") as f:
        res = json.load(f)

    return res


def dump_json(samples, path_):

    with open(path_, "w", encoding="utf-8") as f:
        json.dump(
            samples,
            f,
            ensure_ascii=False,
            indent=2
        )


def load_jsonl(path_):
    list_samples = []
    with open(path_, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            line = line[: -1] if line.endswith(",") else line[: ]
            list_samples.append(
                json.loads(line.strip())
            )

    return list_samples


def dump_jsonl(samples, path_):
    with open(path_, "w", encoding="utf-8") as f:
        for samp in samples:
            f.write(
                json.dumps(samp, ensure_ascii=False) + "\n"
            )


def dump_npy(embeddings, to_path_embed):
    np.save(to_path_embed, embeddings)


def load_npy(path_):
    return np.load(path_)


def dump_memmap(embeddings, to_path_embed):
    memmap = np.memmap(
        to_path_embed,
        shape=embeddings.shape,
        mode="w+",
        dtype=embeddings.dtype
    )

    length = embeddings.shape[0]
    # add in batch
    save_batch_size = 10000
    if length > save_batch_size:
        for i in tqdm(range(0, length, save_batch_size),
                      leave=False,
                      desc="Saving Embeddings"):
            j = min(i + save_batch_size, length)
            memmap[i: j] = embeddings[i: j]
    else:
        memmap[:] = embeddings


def load_memmap_to_float32(vec_file, dim=768):
    embed = np.memmap(
        vec_file,
        mode="r",
        dtype=np.float16
    )
    embed = embed.reshape(-1, dim)
    print("embed: ", embed.shape)

    # embed = embed.tolist()
    # embed_new = np.array(embed, np.float32)
    # print("embed_new: ", embed_new.shape)

    embed_new = []
    for idx in tqdm(range(embed.shape[1])):
        tmp = np.asarray(embed[: , idx])
        tmp = np.array(tmp, np.float32)
        embed_new.append(tmp)

    embed_new = np.stack(embed_new, axis=1)
    print("embed_new: ", embed_new.shape)

    return embed_new


def folder_walk(folder_path):

    list_files = []
    for root, dirs, files in os.walk(folder_path):
        for f in files:
            list_files.append(
                os.path.join(root, f)
            )

    return list_files

# if __name__ == "__main__":
#     vec_file = "./embeddings/combined_wikipedia_50_100.mp"
#     to_path_embed = "./embeddings/combined_wikipedia_50_100_float32.mp"
#     embed_new = load_memmap(vec_file)
#     dump_memmap(embed_new, to_path_embed)