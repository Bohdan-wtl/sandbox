from base.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.locator = MainPageLocators(page)

    def go_to_log_in_page(self):
        self.locator.sign_up_button.click()

    def go_to_sign_up_page(self):
        self.locator.sign_up_button.click()
