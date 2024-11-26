class GeminiRewriterError(Exception):
    """Base exception for Gemini Rewriter."""
    pass

class APIError(GeminiRewriterError):
    """Raised when there's an error with the Gemini API."""
    pass

class ValidationError(GeminiRewriterError):
    """Raised when input validation fails."""
    pass

class ConfigurationError(GeminiRewriterError):
    """Raised when there's a configuration error."""
    pass

class RewriteError(GeminiRewriterError):
    """Raised when text rewriting fails."""
    pass