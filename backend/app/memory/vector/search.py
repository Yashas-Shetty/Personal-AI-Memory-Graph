import logging
from app.memory.vector.client import VectorClient
from app.embeddings.model import EmbeddingModel

logger = logging.getLogger(__name__)

async def semantic_search(query: str, limit: int = 5):
    """
    Search vector store for relevant chunks.
    """
    logger.info(f"Performing semantic search for: {query}")
    
    # 1. Initialize logic
    client = VectorClient()
    embedding_model = EmbeddingModel()
    collection = client.get_collection("memories")

    # 2. Vectorize the query
    query_vector = embedding_model.encode(query)

    # 3. Query Chroma
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=limit
    )

    # 4. Format results
    memories = []
    if results["documents"]:
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            memories.append({
                "content": doc,
                "metadata": meta
            })
    
    return memories
