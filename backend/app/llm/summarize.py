import logging
from app.llm.client import GeminiClient

logger = logging.getLogger(__name__)

async def summarize_memory(text: str) -> str:
    """
    Summarize long text into a concise memory using Gemini.
    """
    if not text or len(text) < 50:
        return text
        
    logger.info("Summarizing text for memory storage")
    
    client = GeminiClient()
    prompt = f"Please summarize the following text into a concise, one-sentence memory: \n\n{text}"
    
    try:
        summary = await client.generate_text(prompt)
        return summary.strip()
    except Exception as e:
        logger.error(f"Summarization failed: {e}")
        return text
