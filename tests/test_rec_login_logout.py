from playwright.sync_api import expect


def test_login_logout(page):
    page.goto("https://app.sibme.com/home/login")

    expect(page.get_by_role("heading", name="Login to Sibme")).to_be_visible()

    page.get_by_role("textbox", name="Email...").fill("usa1")
    page.get_by_role("textbox", name="Password...").fill("Maaja@12")

    page.get_by_role("button", name="SIGN IN").click()

    # Wait for navigation
    page.wait_for_url("**/launchpad")

    # Validate dashboard using reliable locator
    expect(page.get_by_role("heading", name="Test School")).to_be_visible()

    page.get_by_role("heading", name="Test School").click()

    expect(
        page.locator("shared-breadcrumbs").get_by_role("link", name="Home")
    ).to_be_visible()

    page.get_by_text("Usama", exact=True).click()
    expect(page.get_by_text("Logout")).to_be_visible()

    page.wait_for_timeout(3000)

    page.get_by_text("Logout").click()
    expect(page.get_by_role("heading", name="Login to Sibme")).to_be_visible()