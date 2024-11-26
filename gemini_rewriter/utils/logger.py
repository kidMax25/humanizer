import logging
import sys
from typing import Optional
from ..config import config

def setup_logger(name: str = "gemini_rewriter", level: Optional[str] = None) -> logging.Logger:
    """Set up and configure logger."""
    logger = logging.getLogger(name)
    
    # Set log level from config if not specified
    log_level = level or config.log_level
    logger.setLevel(log_level)
    
    # Create console handler if none exists
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(handler)
    
    return logger

logger = setup_logger()