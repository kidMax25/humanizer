from google.generativeai import GenerativeModel
import google.generativeai as genai
import time
import logging
from typing import Optional, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiRewriter:
    def __init__(self, api_key: str):
        """
        Initialize the Gemini Rewriter with API key and configurations.
        
        Args:
            api_key (str): Your Google API key for Gemini access
        """
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        
        # Initialize the model with Gemini Pro
        self.model = GenerativeModel('gemini-pro')
        
        # Rewriting expert prompt
        self.system_prompt = """You are a rewriting expert. Your task is to paraphrase the given text to avoid 
        plagiarism. The rewritten text should effectively communicate the same idea, but with completely different 
        wording. Read and fully understand the original text first, then use your own words to express the same 
        information. The paraphrased text should maintain the same tone and style of the original, while ensuring 
        that it is unique and free from plagiarism. Ensure the rewritten text is grammatically correct and 
        maintains the original meaning."""
        
    async def rewrite_text(self, text: str, max_retries: int = 3, retry_delay: int = 2) -> Optional[str]:
        """
        Rewrite the given text using Gemini AI.
        
        Args:
            text (str): The text to be rewritten
            max_retries (int): Maximum number of retry attempts
            retry_delay (int): Delay between retries in seconds
            
        Returns:
            Optional[str]: The rewritten text, or None if the operation fails
        """
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty")
            
        for attempt in range(max_retries):
            try:
                # Combine system prompt with user's text
                full_prompt = f"{self.system_prompt}\n\nOriginal text:\n{text}\n\nRewritten text:"
                
                # Generate the response
                response = await self.model.generate_content_async(full_prompt)
                
                if response and response.text:
                    logger.info("Successfully rewrote the text")
                    return response.text.strip()
                    
                raise Exception("No response generated")
                
            except Exception as e:
                logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    logger.info(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    logger.error("Max retries reached. Operation failed.")
                    raise
                    
        return None
        
    def check_similarity(self, original_text: str, rewritten_text: str) -> Dict[str, Any]:
        """
        Check the similarity between original and rewritten text.
        This is a placeholder for implementing similarity checks.
        
        Args:
            original_text (str): The original text
            rewritten_text (str): The rewritten text
            
        Returns:
            Dict[str, Any]: Similarity metrics
        """
        # TODO: Implement similarity checking using libraries like:
        # - spacy for semantic similarity
        # - difflib for sequence similarity
        # - rapidfuzz for fuzzy string matching
        pass
        
    def set_custom_prompt(self, prompt: str) -> None:
        """
        Set a custom system prompt for the rewriter.
        
        Args:
            prompt (str): The new system prompt to use
        """
        self.system_prompt = prompt
        logger.info("Updated system prompt")

def main():
    import os
    import asyncio
    from argparse import ArgumentParser
    
    parser = ArgumentParser(description="Rewrite text using Gemini AI")
    parser.add_argument("text", help="Text to rewrite")
    parser.add_argument("--api-key", help="Gemini API key", default=os.getenv("GEMINI_API_KEY"))
    
    args = parser.parse_args()
    
    if not args.api_key:
        print("Please provide a Gemini API key either through --api-key or GEMINI_API_KEY environment variable")
        return
        
    rewriter = GeminiRewriter(args.api_key)
    
    async def run():
        try:
            result = await rewriter.rewrite_text(args.text)
            if result:
                print("\nOriginal text:")
                print(args.text)
                print("\nRewritten text:")
                print(result)
            else:
                print("Failed to rewrite text")
        except Exception as e:
            print(f"Error: {str(e)}")
            
    asyncio.run(run())

if __name__ == "__main__":
    main()