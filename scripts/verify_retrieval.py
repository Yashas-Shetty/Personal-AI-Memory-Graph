import asyncio
import logging
from datetime import datetime
from app.memory.ingest_pipeline import MemoryIngestPipeline
from app.services.reasoning import ReasoningService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    print("\n--- Starting Retrieval & Reasoning Verification ---")
    
    ingest_pipeline = MemoryIngestPipeline()
    reasoning_service = ReasoningService()
    
    # 1. Ingest sample data
    test_text = "I am working on a Personal AI Memory Graph project using FastAPI and ChromaDB. My goal is to finish it tonight."
    print(f"\nIngesting: '{test_text}'")
    await ingest_pipeline.ingest(test_text, source="verification_script", timestamp=datetime.now())
    
    # 2. Wait a bit for Chroma persistence (usually immediate but let's be safe)
    await asyncio.sleep(1)
    
    # 3. Query
    query = "What project am I working on and what tools am I using?"
    print(f"\nQuerying: '{query}'")
    answer = await reasoning_service.reason(query)
    
    print(f"\nAI Answer:\n{answer}")
    print("\n--- Verification Complete ---")

if __name__ == "__main__":
    asyncio.run(main())
