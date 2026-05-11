from playwright.sync_api import Page, expect
from locators.login_locators import LoginLocators

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username_input = page.locator(LoginLocators.USERNAME_INPUT)
        self.password_input = page.locator(LoginLocators.PASSWORD_INPUT)
        self.login_button = page.locator(LoginLocators.SIGN_IN_BTN)
        self.account_name = page.locator(LoginLocators.ACCOUNT_NAME_HDR)

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.page.goto("https://app.sibme.com/home/login")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.page.wait_for_url("**/launchpad")
        expect(self.account_name).to_be_visible()



