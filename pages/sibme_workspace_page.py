from playwright.sync_api import Page, expect
from locators.workspace_locators import WorkspaceLocators

class WorkspacePage:
    def __init__(self, page: Page):
        self.page = page
        # Define Locators using the Locator class
        self.add_new_menu_btn = page.locator(WorkspaceLocators.ADD_NEW_MENU_BTN)
        self.school_header = page.locator(WorkspaceLocators.AUTOMATION_SCHOOL_HDR)
        self.workspace_link = page.locator(WorkspaceLocators.WORKSPACE_LINK)
        self.upload_action_btn = page.locator(WorkspaceLocators.UPLOAD_VIDEO_ACTION_BTN)
        self.file_input = page.locator(WorkspaceLocators.FILE_INPUT_FIELD)
        self.submit_btn = page.locator(WorkspaceLocators.SUBMIT_UPLOAD_BTN)
        self.success_alert = page.locator(WorkspaceLocators.SUCCESS_ALERT)

    def navigate_to_workspace(self):
        self.school_header.click()
        self.workspace_link.click()

    def upload_video_file(self, file_path: str):
        self.add_new_menu_btn.click()
        self.upload_action_btn.click()
        self.file_input.set_input_files(file_path)
        self.submit_btn.click()