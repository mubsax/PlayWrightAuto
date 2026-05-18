import allure
from playwright.sync_api import Page, expect
from locators.launchpad_locators import LaunchpadLocators


class LaunchPage:
    def __init__(self, page: Page):
        self.page = page
        self.multi_account = page.locator(LaunchpadLocators.CHOOSE_ACCOUNT_HDR)
        self.main_account = page.locator(LaunchpadLocators.MAIN_ACCOUNT_HDR)
        self.sub_account = page.locator(LaunchpadLocators.SUB_ACCOUNT_HDR)

    def launch_check(self):
        with allure.step("Verify Launchpad screen layout and accounts"):
            expect(self.multi_account).to_be_visible()
            expect(self.main_account).to_be_visible()
            expect(self.sub_account).to_be_visible()