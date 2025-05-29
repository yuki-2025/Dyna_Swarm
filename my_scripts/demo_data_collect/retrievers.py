import os

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from my_scripts.io_utils import load_json, load_jsonl


def build_faiss_index(corpus_embeddings_path,
                      vector_dim=512,
                      index_factory="Flat"):

    corpus_embeddings = np.load(
        corpus_embeddings_path,
    )
    print("corpus_embeddings: ", corpus_embeddings.shape)

    corpus_embeddings = np.array(corpus_embeddings, np.float32)
    print("corpus_embeddings: ", corpus_embeddings.shape)
    # corpus_embeddings = corpus_embeddings.reshape(-1, vector_dim)
    # print("corpus_embeddings: ", corpus_embeddings.shape)
    # corpus_embeddings = corpus_embeddings.to(np.float32)
    print("corpus_embeddings: ", type(corpus_embeddings))

    vector_dim = corpus_embeddings.shape[-1]
    faiss_index = faiss.IndexFlatIP(vector_dim)
    print("Training Index...")
    faiss_index.train(corpus_embeddings)

    faiss_index.add(corpus_embeddings)
    return faiss_index


class FaissRetriever():
    def __init__(self, demo_data_path,
                 demo_npy_data_path,
                 embed_model=None,):

        self.embed_model = embed_model

        # 加载 faiss index
        self.faiss_index = build_faiss_index(
            demo_npy_data_path,
            vector_dim=512,
            index_factory="Flat"
        )

        # index 对应的 sample
        self.list_samples = load_jsonl(
            demo_data_path
        )

    def search_one_index(self, query_embedding, faiss_index=None, top_k=16):
        scores, indices = faiss_index.search(
            query_embedding, top_k
        )
        scores = scores[0].tolist()
        indices = indices[0].tolist()
        # print("faiss scores in retrievers: ", scores)
        # print("faiss indices: ", indices)
        # 将结果翻译为 样本的原始信息
        list_retrieved_results = []
        for id_, score in zip(indices, scores):
            res = {
                "sample_id": id_,
                "sample": self.list_samples[id_],
                "faiss_score": score
            }
            list_retrieved_results.append(res)

        return list_retrieved_results

    def search_once(self, query, top_k=16, ):

        #  计算图文 embedding
        query_embedding = self.embed_model.encode(
            [query]
        )
        # print("query_embedding: ", query_embedding.shape)

        # 图搜图
        # print("image_embedding: ", image_embedding)
        # print("top_k: ", top_k)
        list_retrieved_results_query2query = self.search_one_index(
            query_embedding,
            faiss_index=self.faiss_index,
            top_k=top_k
        )

        search_results = {}
        search_results["query2query"] = list_retrieved_results_query2query

        return search_results
