"""
Configuration management for the Personal AI Memory Graph system.

This module handles loading and validating environment variables
and application settings.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Attributes:
        APP_NAME: Name of the application
        ENV: Environment (development, production, etc.)
        DEBUG: Debug mode flag
        HOST: Server host address
        PORT: Server port number
    """
    
    APP_NAME: str = "personal-ai-memory-graph"
    ENV: str = "development"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()
