import unittest
import os
import asyncio
from gemini_rewriter import GeminiRewriter

class TestGeminiRewriter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Please set GEMINI_API_KEY environment variable")
        cls.rewriter = GeminiRewriter(api_key)
        
    def setUp(self):
        self.test_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Artificial intelligence is transforming the way we live and work.",
            "Climate change poses significant challenges to our planet's future."
        ]
        
    def test_rewrite_text(self):
        async def run_test():
            for text in self.test_texts:
                result = await self.rewriter.rewrite_text(text)
                self.assertIsNotNone(result)
                self.assertNotEqual(result.strip(), "")
                self.assertNotEqual(result.strip(), text.strip())
                print(f"\nOriginal: {text}")
                print(f"Rewritten: {result}")
                
        asyncio.run(run_test())
        
    def test_empty_input(self):
        async def run_test():
            with self.assertRaises(ValueError):
                await self.rewriter.rewrite_text("")
                
        asyncio.run(run_test())
        
    def test_custom_prompt(self):
        custom_prompt = "Rewrite the text in a more formal tone while maintaining the original meaning."
        self.rewriter.set_custom_prompt(custom_prompt)
        self.assertEqual(self.rewriter.system_prompt, custom_prompt)

if __name__ == "__main__":
    unittest.main(verbosity=2)