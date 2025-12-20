"""
Reasoning service that combines vector, graph, and LLM logic.
"""

from app.memory.retrieve_pipeline import RetrievePipeline
from app.llm.client import GeminiClient
from app.llm.prompts import REASONING_PROMPT

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
        
        if not context:
            context = "No relevant memories found."

        # 2. Construct prompt
        prompt = REASONING_PROMPT.format(context=context, query=user_query)

        # 3. Generate response
        try:
            response = await self.llm.generate_text(prompt)
            return response
        except Exception as e:
            return f"Error generating reasoning: {e}"
        
        return "Reasoned Response based on context"
