from datetime import datetime

def standard_timestamp() -> str:
    """
    Returns current local time as a standardized ISO string.
    """
    return datetime.now().isoformat()

def format_timestamp(dt: datetime) -> str:
    """
    ISO format timestamp.
    """
    return dt.isoformat()
