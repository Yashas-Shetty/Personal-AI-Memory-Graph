"""
API endpoints for memory retrieval.
"""

from fastapi import APIRouter

from app.services.reasoning import ReasoningService

router = APIRouter(prefix="/query", tags=["Memory Retrieval"])
reasoner = ReasoningService()

@router.get("")
async def query_memory(q: str):
    """
    Query the memory system and get a reasoned response.
    """
    answer = await reasoner.reason(q)
    return {"query": q, "answer": answer}
