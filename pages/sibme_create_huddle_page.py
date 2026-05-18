import allure
from playwright.sync_api import Page, expect
from locators.create_huddle_locators import CoachingHuddleLocators


class CoachingHuddle:
    def __init__(self, page: Page):
        self.page = page

        # Define Locators using the Locator class constants
        self.huddles_link = page.locator(CoachingHuddleLocators.HUDDLES_LINK)
        self.huddles_header = page.locator(CoachingHuddleLocators.HUDDLES_HEADER)
        self.add_huddle_btn = page.locator(CoachingHuddleLocators.ADD_HUDDLE_BTN)
        self.create_new_huddle_header = page.locator(CoachingHuddleLocators.CREATE_NEW_HUDDLE_HEADER)
        self.create_first_btn = page.locator(CoachingHuddleLocators.CREATE_FIRST_BTN).first
        self.new_coaching_huddle_header = page.locator(CoachingHuddleLocators.NEW_COACHING_HUDDLE_HEADER)
        self.new_huddle_name_input = page.locator(CoachingHuddleLocators.NEW_HUDDLE_NAME_INPUT)
        self.search_person_input = page.locator(CoachingHuddleLocators.SEARCH_PERSON_INPUT)
        self.person_option = page.locator(CoachingHuddleLocators.PERSON_OPTION)
        self.submit_create_btn = page.locator(CoachingHuddleLocators.SUBMIT_CREATE_BTN)
        self.success_alert = page.locator(CoachingHuddleLocators.SUCCESS_ALERT)


    def navigate_to_huddles(self):
        with allure.step("Navigate to Huddles section"):
            self.huddles_link.click()
            expect(self.huddles_header).to_be_visible()


    def initiate_new_coaching_huddle(self):
        with allure.step("Click Add Huddle and open creation form"):
            self.add_huddle_btn.click()
            expect(self.create_new_huddle_header).to_be_visible()
            self.create_first_btn.click()
            expect(self.new_coaching_huddle_header).to_be_visible()

    def fill_coaching_huddle_details(self, huddle_name: str):
        with allure.step(f"Fill huddle details with name: {huddle_name}"):
            self.new_huddle_name_input.click()
            self.new_huddle_name_input.fill(huddle_name)
            expect(self.search_person_input).to_be_visible(timeout=10000)
            self.search_person_input.click()
            expect(self.person_option).to_be_visible()
            self.person_option.click()

    def submit_coaching_huddle_creation(self):
        with allure.step("Submit huddle creation form and verify success toast"):
            self.submit_create_btn.click()
            expect(self.success_alert).to_be_visible()