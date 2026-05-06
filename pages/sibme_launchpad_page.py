from playwright.sync_api import Page, expect

class LaunchPage:
    def __init__(self, page:Page):
        self.page = page
        self.multi_account = page.get_by_role("heading", name="Choose An Account")
        self.main_account = page.get_by_role("heading", name="Automation School")
        self.sub_account = page.get_by_role("heading", name="Test School")

    def launch_check(self):
        expect(self.multi_account).to_be_visible()
        expect(self.main_account).to_be_visible()
        expect(self.sub_account).to_be_visible()