import os
from pages.sibme_login_page import LoginPage
from dotenv import load_dotenv
import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

load_dotenv()

@pytest.fixture
def launch_page(page):
    username = os.getenv("TEST_USER")
    password = os.getenv("TEST_PASS")

    login_page = LoginPage(page)
    login_page.login(username, password)

    return page


def pytest_sessionfinish(session, exitstatus):
    """Automatically populates the Allure environment widget after the run."""
    allure_results_dir = "my_allure_results"  # Change this if your results directory has a custom name

    if os.path.exists(allure_results_dir):
        env_properties_path = os.path.join(allure_results_dir, "environment.properties")
        with open(env_properties_path, "w") as f:
            f.write("Browser = Chromium\n")
            f.write("Environment = Production\n")
            f.write("Base.URL = https://app.sibme.com\n")
            f.write("Runner = Pytest-Playwright\n")
