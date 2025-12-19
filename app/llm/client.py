import json
import logging
import asyncio
from typing import Optional, Dict, Any

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from app.core.config import settings

logger = logging.getLogger(__name__)


class GeminiClient:
    """
    Clean wrapper for interacting with Google's Gemini API.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini client.
        """
        self.api_key = api_key or settings.GEMINI_API_KEY
        if not self.api_key:
            logger.warning("Gemini API Key not set. LLM features will be disabled.")
            return

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_json(self, prompt: str, timeout: float = 10.0) -> Dict[str, Any]:
        """
        Generates a JSON response from Gemini.
        """
        if not self.api_key:
            logger.error("Attempted to call Gemini API without an API key.")
            return {}

        generation_config = GenerationConfig(
            response_mime_type="application/json"
        )

        try:
            response = await asyncio.wait_for(
                self.model.generate_content_async(
                    contents=prompt,
                    generation_config=generation_config
                ),
                timeout=timeout
            )
            return json.loads(response.text)
        except asyncio.TimeoutError:
            logger.error("Gemini API call timed out.")
            raise
        except Exception as e:
            logger.error(f"Error in Gemini JSON generation: {e}")
            raise

    async def generate_text(self, prompt: str, timeout: float = 10.0) -> str:
        """
        Generates raw text response from Gemini.
        """
        if not self.api_key:
            return ""

        try:
            response = await asyncio.wait_for(
                self.model.generate_content_async(contents=prompt),
                timeout=timeout
            )
            return response.text
        except Exception as e:
            logger.error(f"Error in Gemini text generation: {e}")
            raise
