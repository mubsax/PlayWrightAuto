from playwright.sync_api import Page
from pages.sibme_login_page import LoginPage
from config.settings import Config

def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.login(Config.USER, Config.PASS)