"""
Health check endpoint for the Personal AI Memory Graph system.

This module provides a simple health check endpoint to verify
that the service is running correctly.
"""

from fastapi import APIRouter
from app.core.constants import HEALTH_STATUS_OK, SERVICE_NAME
from app.core.logging import logger

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    
    Returns the service status and name to confirm the service is running.
    
    Returns:
        dict: Service status information
    """
    logger.debug("Health check endpoint called")
    
    return {
        "status": HEALTH_STATUS_OK,
        "service": SERVICE_NAME
    }
