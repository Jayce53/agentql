"""This example demonstrates how to save and load a authenticated state (i.e. signed-in state) using AgentQL."""

import time

from agentql.ext.playwright.sync_api import Page
from playwright.sync_api import sync_playwright

URL = "https://www.yelp.com/"
EMAIL = "REPLACE_WITH_YOUR_EMAIL (For yelp.com)"
PASSWORD = "REPLACE_WITH_YOUR_PASSWORD (For yelp.com)"

# Define the queries to interact with the page
LOG_IN_QUERY = """
{
    log_in_btn
}
"""

CREDENTIALS_QUERY = """
{
    sign_in_form {
        email_input
        password_input
        log_in_btn
    }
}
"""


def save_signed_in_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = browser.new_page()  # type: ignore

        page.goto(URL)

        # Use query_elements() method to locate "Log In" button on the page
        response = page.query_elements(LOG_IN_QUERY)
        # Use Playwright's API to click located button
        response.log_in_btn.click()

        # Use query_elements() method to locate email, password input fields, and "Log In" button in sign-in form
        response_credentials = page.query_elements(CREDENTIALS_QUERY)
        # Fill the email and password input fields
        response_credentials.sign_in_form.email_input.fill(EMAIL)
        response_credentials.sign_in_form.password_input.fill(PASSWORD)
        response_credentials.sign_in_form.log_in_btn.click()

        page.wait_for_page_ready_state()

        # Save the signed-in state
        browser.contexts[0].storage_state(path="yelp_login.json")

        browser.close()


def load_signed_in_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)

        # Load the saved signed-in session by creating a new browser context with the saved signed-in state
        context = browser.new_context(storage_state="yelp_login.json")

        # Create a new page in the broswer and cast it to custom Page type to get access to the AgentQL's querying API
        page: Page = context.new_page()  # type: ignore

        page.goto(URL)

        page.wait_for_page_ready_state()

        # Wait for 5 seconds to see the signed-in page
        time.sleep(5)

        browser.close()


if __name__ == "__main__":
    save_signed_in_state()
    load_signed_in_state()