"""
Orchestrates memory retrieval from vector and graph stores.
"""

import logging

logger = logging.getLogger(__name__)

from app.memory.vector.search import semantic_search
from app.memory.graph.query import get_graph_context

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
        
        # 2. Relationship lookup in graph
        # For each document found, we can look up entities if they were stored in metadata
        # Or we can just look up entities mentioned in the query (advanced)
        # For now, let's just collect the facts found in the vector search.
        
        context_parts = []
        for res in vector_results:
            context_parts.append(f"Memory: {res['content']}")
        
        # 3. Aggregate all context
        return "\n".join(context_parts)
