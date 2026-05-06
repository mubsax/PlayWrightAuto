from pages.sibme_launchpad_page import LaunchPage


def test_launchpad_accounts(launch_page):
    l_page = LaunchPage(launch_page)
    l_page.launch_check()



