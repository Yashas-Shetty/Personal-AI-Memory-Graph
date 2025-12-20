"""
Centralized logging configuration for the Personal AI Memory Graph system.

This module sets up the logging system with configurable log levels
and formatting.
"""

import logging
import sys
from app.core.config import settings


def setup_logging() -> logging.Logger:
    """
    Configure and return the application logger.
    
    Sets up console logging with appropriate formatting and log level
    based on the application configuration.
    
    Returns:
        logging.Logger: Configured logger instance
    """
    # Determine log level based on DEBUG setting
    log_level = logging.DEBUG if settings.DEBUG else logging.INFO
    
    # Create logger
    logger = logging.getLogger(settings.APP_NAME)
    logger.setLevel(log_level)
    
    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Add formatter to handler
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger


# Global logger instance
logger = setup_logging()
