import unittest
from humanizer import humanizer

class TestHumanizer(unittest.TestCase):
    def test_process_text(self):
        input_text = "This is a test input for the Humanize AI tool."
        output = humanizer.process_text(input_text)
        self.assertIsNotNone(output)
        print("Output:", output)

if __name__ == "__main__":
    unittest.main()
