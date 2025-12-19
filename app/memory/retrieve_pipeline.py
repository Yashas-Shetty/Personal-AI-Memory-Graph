"""
Orchestrates memory retrieval from vector and graph stores.
"""

import logging

logger = logging.getLogger(__name__)

from app.memory.vector.search import semantic_search
from app.memory.graph.query import build_entity_query

class RetrievePipeline:
    """
    Pipeline for querying the memory system.
    """
    def __init__(self):
        pass

    async def retrieve(self, query: str):
        """
        Search for relevant memories from both vector and graph stores.
        """
        logger.info(f"Retrieving memories for query: {query}")
        
        # 1. Semantic search in vector store
        vector_results = await semantic_search(query)
        
        # 2. Relationship lookup in graph (simplified)
        # graph_results = await some_graph_lookup(query)
        
        return vector_results
