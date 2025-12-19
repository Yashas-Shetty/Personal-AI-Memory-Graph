"""
API endpoints for memory inspection and debugging.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/memory", tags=["Memory Management"])

@router.get("/inspect")
async def inspect_memory():
    """
    List or inspect recent memories.
    """
    return {"memories": []}
