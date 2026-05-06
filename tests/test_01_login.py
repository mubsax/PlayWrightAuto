import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.sibme_login_page import LoginPage

load_dotenv()

def test_login(page: Page) -> None:
    username = os.getenv("TEST_USER")
    password = os.getenv("TEST_PASS")

    login_page = LoginPage(page)
    login_page.login(username, password)