from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class IngestRequest(BaseModel):
    text: str = Field(..., description="User input text to store as memory")
    source: str = Field(..., description="Source of memory: chat | note | idea | task")
    timestamp: Optional[datetime] = Field(
        default_factory=datetime.utcnow,
        description="Time when the memory was created"
    )


class IngestResponse(BaseModel):
    status: str
    message: str
