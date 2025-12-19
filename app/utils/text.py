"""
Text processing utilities.
"""

def clean_text(text: str) -> str:
    """
    Basic text cleaning.
    """
    return text.strip()

def chunk_text(text: str, size: int = 500) -> list[str]:
    """
    Split text into chunks.
    """
    return [text[i:i+size] for i in range(0, len(text), size)]
