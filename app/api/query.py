"""
API endpoints for memory retrieval.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/query", tags=["Memory Retrieval"])

@router.get("")
async def query_memory(q: str):
    """
    Query the memory system.
    """
    return {"query": q, "results": []}
