import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional

# Load environment variables
load_dotenv()

@dataclass
class Config:
    """Configuration settings for the Gemini Rewriter."""
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    model_name: str = "gemini-pro"
    max_retries: int = 3
    retry_delay: int = 2
    timeout: int = 30
    log_level: str = "INFO"
    
    def validate(self) -> None:
        """Validate the configuration settings."""
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY must be set")
            
config = Config()