import unittest
import logging
import sys
import os

# Add the parent directory to sys.path to allow imports from the humanizer package
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humanizer.humanizer import process_text

class TestHumanizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.INFO)
    
    def setUp(self):
        self.short_text = "This is a test input for the Humanize AI tool."
        self.long_text = "This is a longer test input that contains multiple sentences. " * 5
    
    def test_short_text(self):
        try:
            output = process_text(self.short_text)
            self.assertIsNotNone(output)
            self.assertNotEqual(output.strip(), "")
            self.assertNotEqual(output.strip(), self.short_text.strip())
            print(f"\nInput: {self.short_text}")
            print(f"Output: {output}")
        except Exception as e:
            self.fail(f"process_text raised an exception: {str(e)}")
    
    def test_long_text(self):
        try:
            output = process_text(self.long_text)
            self.assertIsNotNone(output)
            self.assertNotEqual(output.strip(), "")
            self.assertNotEqual(output.strip(), self.long_text.strip())
            print(f"\nInput: {self.long_text}")
            print(f"Output: {output}")
        except Exception as e:
            self.fail(f"process_text raised an exception: {str(e)}")
    
    def test_empty_input(self):
        with self.assertRaises(ValueError):
            process_text("")
    
    def test_whitespace_input(self):
        with self.assertRaises(ValueError):
            process_text("   ")

if __name__ == "__main__":
    unittest.main(verbosity=2)