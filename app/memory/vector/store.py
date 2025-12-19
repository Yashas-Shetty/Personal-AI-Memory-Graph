import logging

logger = logging.getLogger(__name__)


class VectorMemoryStore:
    """
    Stub interface for vector memory storage.
    Actual ChromaDB logic will be implemented later.
    """

    def store_memory(self, payload: dict) -> None:
        """
        Store memory payload into vector database.
        """
        logger.info("Vector store called with payload")
        logger.debug(payload)
        # No implementation yet
        return
