"""
API endpoints for memory inspection and debugging.
"""

from fastapi import APIRouter
from app.core.logging import logger

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
    
    vector_count = 0
    graph_count = 0
    status = "online"
    
    try:
        vector_count = vector_client.count()
    except Exception as e:
        logger.warning(f"Vector store not ready: {e}")
        status = "partial_failure"

    try:
        graph_count = graph_client.count_nodes()
    except Exception as e:
        logger.warning(f"Graph store not connected (Neo4j): {e}")
        status = "partial_failure" if status == "online" else "offline"
        
    return {
        "vector_count": vector_count,
        "graph_count": graph_count,
        "status": status
    }

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

@router.get("/list")
async def list_memories(source: str = None):
    """
    List stored memories, optionally filtered by source (note, task, idea, chat).
    """
    vector_client = VectorClient()
    try:
        memories = vector_client.list_memories(source=source)
        return {"memories": memories}
    except Exception as e:
        logger.error(f"Failed to list memories: {e}")
        return {"error": str(e), "memories": []}

@router.get("/inspect")
async def inspect_memory():
    """
    List or inspect recent memories.
    """
    # For now, just return stats link or simplified list
    return {"message": "Use /stats for counts or /query to search."}
