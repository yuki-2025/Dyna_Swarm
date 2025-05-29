import torch.nn as nn
from sentence_transformers import SentenceTransformer


class EmbedModel(nn.Module):
    def __init__(
            self,
            model_name_or_path: str = None,
    ) -> None:
        super(EmbedModel, self).__init__()

        self.embed_model = SentenceTransformer(
            model_name_or_path,
            # torch_dtype=torch.bfloat16
        ).to("cuda")

    def encode_batch_pairs(self,
                           queries,):
        '''
        This function will be used for retrieval task
        if there is a instruction for queries, we will add it to the query text
        '''
        text_embeds = self.embed_model.encode(queries, normalize_embeddings=True)

        return text_embeds















