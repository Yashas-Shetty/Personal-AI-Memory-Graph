"""
Reasoning service that combines vector, graph, and LLM logic.
"""

from app.memory.retrieve_pipeline import RetrievePipeline
from app.llm.client import GeminiClient

class ReasoningService:
    """
    Brain of the system that merges different memory layers.
    """
    def __init__(self):
        self.retriever = RetrievePipeline()
        self.llm = GeminiClient()

    async def reason(self, user_query: str):
        """
        Produce a reasoned response based on retrieved context.
        """
        # 1. Retrieve context
        context = await self.retriever.retrieve(user_query)
        
        # 2. Reason over context
        return "Reasoned Response based on context"
