# Humanizer

A Python package to automate text processing using Humanize AI with Playwright.

## Installation

```bash
pip install playwright
playwright install
pip install .
```

#### **Usage Example**
```python
from humanizer.humanizer import Humanizer

humanizer = Humanizer()
input_text = "This is a simple example to test the humanizer package."
output = humanizer.process_text(input_text)
print("Output:", output)