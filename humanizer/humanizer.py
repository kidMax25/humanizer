from playwright.sync_api import sync_playwright

def process_text(text):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Open the website
        page.goto("https://www.humanizeai.pro/")

        # Wait for the textarea to appear
        textarea_selector = "textarea.InputContainer_inputContainer__jeGwX"
        page.wait_for_selector(textarea_selector, timeout=60000)  # Wait up to 60 seconds
        page.fill(textarea_selector, text)

        # Click the paraphrase button
        button_selector = "button.ParaphraseButton_button__nWdlZ"
        page.click(button_selector)

        # Wait for the output copy button to appear (indicating that processing is done)
        copy_button_selector = "img[title='Copy to clipboard']"
        page.wait_for_selector(copy_button_selector, timeout=120000)  # Wait up to 120 seconds for the output

        # Extract the final output from the relevant div
        output_selector = "div.OutputContainer_output__wvgeh span.Editor_t__not_edited_long__JuNNx"
        output_element = page.query_selector(output_selector)
        output = output_element.inner_text() if output_element else None

        browser.close()
        return output
