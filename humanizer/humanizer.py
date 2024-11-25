from playwright.sync_api import sync_playwright
import time
import logging
import random
from typing import Optional, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProxyRotator:
    def __init__(self, proxy_list: List[str]):
        self.proxies = proxy_list
        self.current_index = 0
    
    def get_next_proxy(self) -> str:
        proxy = self.proxies[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.proxies)
        return proxy

def process_text(text: str, proxy_list: Optional[List[str]] = None, max_retries=3, retry_delay=5):
    """
    Process text using HumanizeAI with proxy rotation.
    """
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty")
    
    proxy_rotator = ProxyRotator(proxy_list) if proxy_list else None
    
    for attempt in range(max_retries):
        try:
            with sync_playwright() as p:
                proxy = proxy_rotator.get_next_proxy() if proxy_rotator else None
                
                context_args = {
                    "viewport": {"width": 1920, "height": 1080},
                }
                
                if proxy:
                    context_args["proxy"] = {
                        "server": proxy,
                        "username": "YOUR_PROXY_USERNAME",  # if required
                        "password": "YOUR_PROXY_PASSWORD",  # if required
                    }
                
                browser = p.chromium.launch(headless=False)
                context = browser.new_context(**context_args)
                page = context.new_page()
                
                # Rest of the code remains the same...
                # (Previous implementation of text processing)
                
                return output
                
        except Exception as e:
            logger.error(f"Attempt {attempt + 1} failed with proxy: {proxy if proxy else 'No proxy'}: {str(e)}")
            if attempt < max_retries - 1:
                logger.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                logger.error("Max retries reached. Operation failed.")
                raise

# Example usage with proxy list
proxy_list = [
    "91.65.103.3:80",
    "91.148.134.48:80",
    # Add more proxies
]

result = process_text("Your text here", proxy_list=proxy_list)