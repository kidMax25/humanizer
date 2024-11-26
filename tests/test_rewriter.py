import unittest
import asyncio
import os
from dotenv import load_dotenv
from gemini_rewriter.rewriter import GeminiRewriter
from gemini_rewriter.exceptions import ValidationError

# Load environment variables
load_dotenv()

class TestGeminiRewriter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test class with API key and rewriter instance."""
        cls.api_key = os.getenv("GEMINI_API_KEY")
        if not cls.api_key:
            raise ValueError("Please set GEMINI_API_KEY in .env file or environment variables")
        
    def setUp(self):
        """Set up test cases and create a new rewriter instance for each test."""
        self.rewriter = GeminiRewriter(self.api_key)
        self.test_cases = [
            {
                "input": "The quick brown fox jumps over the lazy dog.",
                "description": "Simple sentence"
            },
            {
                "input": """Artificial intelligence is transforming modern society. 
                           It affects how we work, communicate, and live our daily lives.""",
                "description": "Multi-sentence paragraph"
            },
            {
                "input": "Python is a high-level programming language known for its simplicity and readability.",
                "description": "Technical content"
            }
        ]
        
        # Create new event loop for each test
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        
    def tearDown(self):
        """Clean up the event loop after each test."""
        self.loop.close()

    def test_rewrite_basic(self):
        """Test basic text rewriting functionality."""
        async def run_test():
            for case in self.test_cases:
                print(f"\nTesting: {case['description']}")
                print(f"Input: {case['input']}")
                result = await self.rewriter.rewrite_text(case["input"])
                print(f"Output: {result}\n")
                
                self.assertIsNotNone(result)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)
                self.assertNotEqual(result.lower(), case["input"].lower())
                
        self.loop.run_until_complete(run_test())

    def test_empty_input(self):
        """Test handling of empty input."""
        async def run_test():
            with self.assertRaises(ValueError):
                await self.rewriter.rewrite_text("")
                
        self.loop.run_until_complete(run_test())

    def test_whitespace_input(self):
        """Test handling of whitespace-only input."""
        async def run_test():
            with self.assertRaises(ValueError):
                await self.rewriter.rewrite_text("   ")
                
        self.loop.run_until_complete(run_test())

    def test_custom_prompt(self):
        """Test custom prompt functionality."""
        async def run_test():
            custom_prompt = "Rewrite this in a more formal academic style:"
            self.rewriter.set_custom_prompt(custom_prompt)
            
            test_text = "The car is really fast."
            result = await self.rewriter.rewrite_text(test_text)
            
            self.assertIsNotNone(result)
            print(f"\nCustom prompt test:")
            print(f"Input: {test_text}")
            print(f"Output: {result}")
            
        self.loop.run_until_complete(run_test())

if __name__ == "__main__":
    unittest.main(verbosity=2)