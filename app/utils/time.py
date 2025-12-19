"""
Time-related helper functions.
"""

from datetime import datetime

def format_timestamp(dt: datetime) -> str:
    """
    ISO format timestamp.
    """
    return dt.isoformat()
