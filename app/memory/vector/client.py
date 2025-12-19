"""
Vector memory client (Chroma placeholder).
"""

import chromadb
from chromadb.config import Settings as ChromaSettings
from app.core.config import settings

class VectorClient:
    """
    Client for interacting with ChromaDB.
    """
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PERSIST_DIRECTORY,
            settings=ChromaSettings(allow_reset=True)
        )

    def get_collection(self, name: str = "memories"):
        """
        Get or create a collection.
        """
        return self.client.get_or_create_collection(name=name)

    def count(self, collection_name: str = "memories") -> int:
        """
        Return the number of items in the collection.
        """
        collection = self.get_collection(collection_name)
        return collection.count()

    def reset(self):
        """
        Reset the entire database.
        """
        self.client.reset()
