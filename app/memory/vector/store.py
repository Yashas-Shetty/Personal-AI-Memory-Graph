import logging

logger = logging.getLogger(__name__)


import logging
from datetime import datetime
from uuid import uuid4

from app.memory.vector.client import VectorClient
from app.embeddings.model import EmbeddingModel

logger = logging.getLogger(__name__)


class VectorMemoryStore:
    """
    Vector memory storage using ChromaDB.
    """

    def __init__(self):
        self.client = VectorClient()
        self.embedding_model = EmbeddingModel()
        self.collection = self.client.get_collection("memories")

    def store_memory(self, payload: dict) -> None:
        """
        Store memory payload into vector database.
        """
        logger.info("Storing memory in Vector Store")
        
        text = payload.get("text", "")
        if not text:
            logger.warning("Attempted to store empty text in Vector Store.")
            return

        # 1. Generate embedding
        vector = self.embedding_model.encode(text)

        # 2. Prepare metadata
        metadata = {
            "source": payload.get("source", "unknown"),
            "timestamp": payload.get("timestamp", datetime.now().isoformat()),
        }

        # 3. Store in Chroma
        id = str(uuid4())
        self.collection.add(
            ids=[id],
            embeddings=[vector],
            metadatas=[metadata],
            documents=[text]
        )
        
        logger.info(f"Memory stored in Vector DB with ID: {id}")
