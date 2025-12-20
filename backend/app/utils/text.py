import re

def clean_text(text: str) -> str:
    """
    Basic text cleaning: remove extra whitespace and normalize.
    """
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def truncate_text(text: str, max_length: int = 500) -> str:
    """
    Truncate text to a maximum length.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length-3] + "..."

def chunk_text(text: str, size: int = 500) -> list[str]:
    """
    Split text into chunks.
    """
    return [text[i:i+size] for i in range(0, len(text), size)]
