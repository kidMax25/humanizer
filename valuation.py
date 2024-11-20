from playwright.sync_api import sync_playwright

def check_class_exists():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.humanizeai.pro/")

        # Check for the output container
        exists = page.locator(".OutputContainer_outputContainer__PvVjd").count() > 0
        print("Class exists on the page." if exists else "Class does not exist.")

        browser.close()

check_class_exists()
