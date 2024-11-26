import asyncio
import os
from dotenv import load_dotenv
from gemini_rewriter import GeminiRewriter

async def main():
    # Load environment variables
    load_dotenv()
    
    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set GEMINI_API_KEY in .env file or environment variables")
        
    # Initialize rewriter
    rewriter = GeminiRewriter(api_key)
    
    # Test text
    test_text = """
    Artificial intelligence is rapidly transforming the modern world. 
    From autonomous vehicles to smart assistants, AI technologies are 
    becoming increasingly integrated into our daily lives. This integration 
    brings both opportunities and challenges that society must address.
    """
    
    try:
        # Rewrite the text
        print("Original text:")
        print(test_text)
        print("\nProcessing...\n")
        
        result = await rewriter.rewrite_text(test_text)
        
        print("Rewritten text:")
        print(result)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())