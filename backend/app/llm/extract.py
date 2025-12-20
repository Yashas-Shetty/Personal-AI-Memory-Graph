"""
Extraction logic for entities and relationships using Gemini.
"""

import logging
import asyncio
from typing import Optional

from pydantic import ValidationError

from app.llm.client import GeminiClient
from app.llm.schemas import ExtractionResult, RelationshipType
from app.llm.prompts import ENTITY_EXTRACTION_PROMPT

logger = logging.getLogger(__name__)


async def extract_from_text(text: str, client: Optional[GeminiClient] = None) -> ExtractionResult:
    """
    Extracts structured data from text using Gemini with retries.
    """
    if client is None:
        client = GeminiClient()

    if not client.api_key:
        return ExtractionResult(entities=[], relationships=[])

    valid_types = ", ".join(RelationshipType.__args__)
    prompt = ENTITY_EXTRACTION_PROMPT.format(text=text, valid_types=valid_types)

    retries = 3
    for attempt in range(retries):
        try:
            logger.info(f"Extracting entities: Attempt {attempt + 1}/{retries}")
            data = await client.generate_json(prompt)
            return ExtractionResult(**data)
        except Exception as e:
            logger.warning(f"Extraction attempt {attempt + 1} failed: {e}")
            await asyncio.sleep(1)

    logger.error("All extraction attempts failed.")
    return ExtractionResult(entities=[], relationships=[])
