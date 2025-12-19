import logging
from datetime import datetime

from app.memory.vector.store import VectorMemoryStore
from app.memory.graph.store import GraphMemoryStore
from app.llm.extract import extract_from_text

logger = logging.getLogger(__name__)


class MemoryIngestPipeline:
    """
    Orchestrates the memory ingestion flow.
    """

    def __init__(self):
        self.vector_store = VectorMemoryStore()
        self.graph_store = GraphMemoryStore()

    async def ingest(self, text: str, source: str, timestamp: datetime) -> None:
        """
        Main ingestion entrypoint.
        """
        logger.info("Starting memory ingestion pipeline")

        # 1. Extract Intelligence (Entities & Relationships)
        extraction_result = await extract_from_text(text)
        
        # 2. Prepare Payload
        payload = self._prepare_payload(text, source, timestamp, extraction_result)

        # 3. Store Data
        # Note: Stores are currently synchronous stubs. 
        # In a real async DB scenario, these would also be awaited.
        self.vector_store.store_memory(payload)
        
        if extraction_result.entities:
            self.graph_store.store_memory(payload)
        else:
            logger.warning("Skipping graph storage: No entities extracted or LLM failure.")

        logger.info("Memory ingestion pipeline completed")

    def _prepare_payload(self, text: str, source: str, timestamp: datetime, extraction_result) -> dict:
        """
        Normalize and prepare memory payload.
        """
        logger.debug("Preparing memory payload")

        return {
            "text": text.strip(),
            "source": source,
            "timestamp": timestamp.isoformat(),
            "extraction": extraction_result.dict(),
        }
