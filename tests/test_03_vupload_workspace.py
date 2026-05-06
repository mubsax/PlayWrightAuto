from pages.sibme_launchpad_page import LaunchPage
from playwright.sync_api import expect
from pathlib import Path

def upload_video(page, file_name):

    video_path = Path(__file__).parent.parent / "videos" / file_name
    page.set_input_files("input[type='file']", str(video_path))

def test_vupload_workspace(launch_page):
    workspace_page = LaunchPage(launch_page)
    workspace_page.launch_check()

    workspace_page.page.get_by_role("heading", name="Automation School").click()
    expect(workspace_page.page.locator("label").filter(has_text="Home")).to_be_visible()
    workspace_page.page.get_by_role("link", name="Workspace").click()
    workspace_page.page.wait_for_timeout(5000)
    expect(workspace_page.page.get_by_role("heading", name="My Workspace")).to_be_visible()
    workspace_page.page.get_by_role("button").first.click()
    workspace_page.page.get_by_text("Upload Video").click()
    expect(workspace_page.page.get_by_text("Select Files to Upload or"))
    upload_video(workspace_page.page, "test_video.MP4")
    workspace_page.page.get_by_role("button", name="Upload", exact=True).click()

    alert_locator = workspace_page.page.get_by_role("alert", name="New Video Uploaded")
    expect(alert_locator).to_be_visible(timeout=30000)
