import allure
from pages.sibme_launchpad_page import LaunchPage

@allure.epic("Core Functionality")
@allure.feature("Launchpad")
@allure.story("Verify Launchpad Accounts")
@allure.severity(allure.severity_level.CRITICAL)
def test_launchpad_accounts(launch_page):
    l_page = LaunchPage(launch_page)
    l_page.launch_check()



