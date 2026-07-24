from sentence_transformers import SentenceTransformer

from app.config.setting import settings


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL
        )

    def encode(self, text):

        embeddings = self.model.encode(text)

        return embeddings.tolist()


embedding_model = EmbeddingModel()