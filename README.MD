# Gemini Rewriter

A Python package that uses Google's Gemini AI to rewrite and paraphrase text while maintaining the original meaning and context.

## Installation

```bash
pip install gemini-rewriter
```

## Quick Start

```python
import asyncio
from gemini_rewriter import GeminiRewriter

async def main():
    rewriter = GeminiRewriter('your_api_key_here')
    result = await rewriter.rewrite_text("Your text to rewrite")
    print(result)

asyncio.run(main())
```

## Command Line Usage

```bash
gemini-rewrite "Your text to rewrite" --api-key your_api_key_here
```

## Features

- Async support for better performance
- Retry mechanism for reliability
- Customizable system prompt
- Proper error handling and logging
- CLI interface
- Input validation
- Comprehensive logging

## Configuration

Create a `.env` file in your project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install in development mode: `pip install -e .`
4. Run tests: `python -m unittest discover tests`

## License

MIT License