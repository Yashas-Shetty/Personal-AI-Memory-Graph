import logging
from datetime import datetime

from app.memory.vector.store import VectorMemoryStore
from app.memory.graph.store import GraphMemoryStore

logger = logging.getLogger(__name__)


class MemoryIngestPipeline:
    """
    Orchestrates the memory ingestion flow.
    """

    def __init__(self):
        self.vector_store = VectorMemoryStore()
        self.graph_store = GraphMemoryStore()

    def ingest(self, text: str, source: str, timestamp: datetime) -> None:
        """
        Main ingestion entrypoint.
        """
        logger.info("Starting memory ingestion pipeline")

        payload = self._prepare_payload(text, source, timestamp)

        self.vector_store.store_memory(payload)
        self.graph_store.store_memory(payload)

        logger.info("Memory ingestion pipeline completed")

    def _prepare_payload(self, text: str, source: str, timestamp: datetime) -> dict:
        """
        Normalize and prepare memory payload.
        """
        logger.debug("Preparing memory payload")

        return {
            "text": text.strip(),
            "source": source,
            "timestamp": timestamp.isoformat(),
        }
