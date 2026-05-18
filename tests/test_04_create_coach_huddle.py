import allure
from pages.sibme_launchpad_page import LaunchPage
from pages.sibme_workspace_page import WorkspacePage
from pages.sibme_create_huddle_page import CoachingHuddle


@allure.epic("Core Functionality")
@allure.feature("Huddles")
@allure.story("Create Coaching Huddle")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_coaching_huddle_successfully(launch_page):
    # Initialize Pages using the launch_page fixture
    lp = LaunchPage(launch_page)
    wp = WorkspacePage(launch_page)
    huddle_page = CoachingHuddle(launch_page)

    # Execution steps
    lp.launch_check()
    wp.navigate_to_workspace()
    huddle_page.navigate_to_huddles()
    huddle_page.initiate_new_coaching_huddle()
    huddle_page.fill_coaching_huddle_details("test coach")
    huddle_page.submit_coaching_huddle_creation()