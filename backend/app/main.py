"""
Main entry point for the Personal AI Memory Graph system.

This module initializes the FastAPI application,
registers middleware, and attaches core routes.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api.ingest import router as ingest_router
from app.api.query import router as query_router
from app.api.memory import router as memory_router

from app.core.config import settings
from app.core.logging import logger
from app.core.constants import APP_VERSION, APP_DESCRIPTION
from app.api import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan handler.

    Used for startup and shutdown events.
    """
    logger.info("🚀 Personal AI Memory Graph starting up...")
    logger.info(f"Environment: {settings.ENV}")
    logger.info(f"Debug mode: {settings.DEBUG}")

    # Startup logic goes here (later: DB connections, memory engines)
    yield

    # Shutdown logic goes here
    logger.info("🛑 Personal AI Memory Graph shutting down...")
    
    # Close Graph connection if it exists
    from app.memory.graph.client import GraphClient
    # This is a bit hacky as we don't have a singleton, but good for structural demo
    try:
        GraphClient().close()
    except:
        pass


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance
    """
    app = FastAPI(
        title=settings.APP_NAME,
        description=APP_DESCRIPTION,
        version=APP_VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan
    )

    # -------------------------
    # Middleware
    # -------------------------
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # -------------------------
    # Routes
    # -------------------------
    @app.get("/", tags=["Root"])
    async def root():
        return {
            "message": "Welcome to the Personal AI Memory Graph API",
            "docs": "/docs",
            "health": "/health"
        }

    app.include_router(health.router, tags=["Health"])
    app.include_router(ingest_router)
    app.include_router(query_router)
    app.include_router(memory_router)

    logger.info(f"Application '{settings.APP_NAME}' initialized")

    return app


# Create the application instance
app = create_application()


if __name__ == "__main__":
    logger.info(f"Starting server on {settings.HOST}:{settings.PORT}")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
