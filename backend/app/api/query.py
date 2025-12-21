"""
API endpoints for memory retrieval.
"""

from fastapi import APIRouter

from app.services.reasoning import ReasoningService

router = APIRouter(prefix="/query", tags=["Memory Retrieval"])
reasoner = ReasoningService()

@router.post("/reason")
async def query_memory(query: str):
    """
    Query the memory system and get a reasoned response.
    """
    answer = await reasoner.reason(query)
    return answer  # Returns raw string which FastAPI wraps in JSON
