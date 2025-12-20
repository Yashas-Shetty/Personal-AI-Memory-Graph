"""
Configuration management for the Personal AI Memory Graph system.

This module handles loading and validating environment variables
and application settings.
"""

from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Attributes:
        APP_NAME: Name of the application
        ENV: Environment (development, production, etc.)
        DEBUG: Debug mode flag
        HOST: Server host address
        PORT: Server port number
        CORS_ORIGINS: Allowed CORS origins
    """
    
    APP_NAME: str = "personal-ai-memory-graph"
    ENV: str = "development"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Gemini Settings
    GEMINI_API_KEY: Optional[str] = None
    
    # Neo4j Settings
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "password"
    
    # Chroma Settings
    CHROMA_PERSIST_DIRECTORY: str = "./data/chroma"

    # CORS configuration
    CORS_ORIGINS: List[str] = [
        "*", 
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
