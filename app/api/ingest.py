from fastapi import APIRouter

from app.schemas.ingest import IngestRequest, IngestResponse
from app.memory.ingest_pipeline import MemoryIngestPipeline

router = APIRouter(prefix="/ingest", tags=["Memory Ingestion"])

pipeline = MemoryIngestPipeline()


@router.post("", response_model=IngestResponse)
def ingest_memory(request: IngestRequest):
    pipeline.ingest(
        text=request.text,
        source=request.source,
        timestamp=request.timestamp,
    )

    return IngestResponse(
        status="accepted",
        message="Memory ingestion started",
    )
