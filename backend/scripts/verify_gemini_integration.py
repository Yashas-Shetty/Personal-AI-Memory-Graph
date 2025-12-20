import asyncio
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from app.memory.ingest_pipeline import MemoryIngestPipeline
from app.core.config import settings

async def main():
    print("--- Starting Gemini Integration Verification ---")
    
    # 1. Check Config
    print(f"API Key present: {'Yes' if settings.GEMINI_API_KEY else 'No'}")
    
    # 2. Check Pipeline Instantiation
    try:
        pipeline = MemoryIngestPipeline()
        print("Pipeline instantiated successfully.")
    except Exception as e:
        print(f"Failed to instantiate pipeline: {e}")
        return

    # 3. Test Ingestion
    text = "I want to learn Flask to build my internship project"
    source = "test_script"
    timestamp = datetime.now()
    
    print(f"Ingesting text: '{text}'")
    try:
        await pipeline.ingest(text, source, timestamp)
        print("Ingestion call completed without error.")
    except Exception as e:
        print(f"Ingestion failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
