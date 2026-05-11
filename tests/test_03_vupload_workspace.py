from pages.sibme_launchpad_page import LaunchPage
from pages.sibme_workspace_page import WorkspacePage
from playwright.sync_api import expect
from pathlib import Path


def test_vupload_workspace(launch_page):
    # Initialize Pages
    lp = LaunchPage(launch_page)
    wp = WorkspacePage(launch_page)

    # Execution
    lp.launch_check()
    wp.navigate_to_workspace()

    # Define file path
    video_path = Path(__file__).parent.parent / "videos" / "test_video.mp4"

    # Perform Upload
    wp.upload_video_file(str(video_path))

    # Assertions
    expect(wp.success_alert).to_be_visible(timeout=30000)