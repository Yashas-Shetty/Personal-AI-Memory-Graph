"""
Embedding model loading logic.
"""

from fastembed import TextEmbedding
from typing import List

class EmbeddingModel:
    """
    Provides local embeddings using fastembed.
    Default model: BAAI/bge-small-en-v1.5
    """
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        self.model = TextEmbedding(model_name=model_name)

    def encode(self, text: str) -> List[float]:
        """
        Convert text to vector.
        """
        # fastembed returns a generator of numpy arrays
        embeddings = list(self.model.embed([text]))
        return embeddings[0].tolist()
