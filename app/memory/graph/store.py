import logging

logger = logging.getLogger(__name__)


class GraphMemoryStore:
    """
    Stub interface for graph memory storage.
    Actual Neo4j logic will be implemented later.
    """

    def store_memory(self, payload: dict) -> None:
        """
        Store memory payload into graph database.
        """
        logger.info("Graph store called with payload")
        logger.debug(payload)
        # No implementation yet
        return
