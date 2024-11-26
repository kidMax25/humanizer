from typing import Optional
from ..exceptions import ValidationError

def validate_input_text(text: str) -> None:
    """Validate input text."""
    if not text:
        raise ValidationError("Input text cannot be empty")
    if not isinstance(text, str):
        raise ValidationError("Input text must be a string")
    if not text.strip():
        raise ValidationError("Input text cannot be only whitespace")
    if len(text.strip()) < 3:
        raise ValidationError("Input text must be at least 3 characters long")

def validate_api_key(api_key: Optional[str]) -> None:
    """Validate API key."""
    if not api_key:
        raise ValidationError("API key cannot be empty")
    if not isinstance(api_key, str):
        raise ValidationError("API key must be a string")
    if not api_key.strip():
        raise ValidationError("API key cannot be only whitespace")