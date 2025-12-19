"""
API endpoints for memory inspection and debugging.
"""

from fastapi import APIRouter

from app.memory.vector.client import VectorClient
from app.memory.graph.client import GraphClient

router = APIRouter(prefix="/memory", tags=["Memory Management"])

@router.get("/stats")
async def get_memory_stats():
    """
    Get basic statistics about stored memories.
    """
    vector_client = VectorClient()
    graph_client = GraphClient()
    
    try:
        vector_count = vector_client.count()
        graph_count = graph_client.count_nodes()
        
        return {
            "vector_count": vector_count,
            "graph_count": graph_count,
            "status": "online"
        }
    except Exception as e:
        return {"error": str(e), "status": "partial_failure"}

@router.post("/clear")
async def clear_all_memory():
    """
    DANGER: Permanently delete all stored memories from vector and graph stores.
    """
    vector_client = VectorClient()
    graph_client = GraphClient()
    
    try:
        # Note: Chroma reset depends on settings.CHROMA_ALLOW_RESET
        # For our persistent client we set the config during initialization.
        vector_client.reset()
        graph_client.clear_database()
        
        return {"message": "All memories cleared successfully."}
    except Exception as e:
        return {"error": str(e), "message": "Failed to clear some storage layers."}

@router.get("/inspect")
async def inspect_memory():
    """
    List or inspect recent memories.
    """
    # For now, just return stats link or simplified list
    return {"message": "Use /stats for counts or /query to search."}
