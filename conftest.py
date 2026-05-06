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

