from base.base_page import BasePage
from new_pages.locators.qr_creation_flow_locators import QrCreationLocators
from utils import generation_test_data

class QrCreationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = QrCreationLocators(self)

    #DPF Flow with select_dpf_plan function
    def select_dpf_plan(self):
        self.locator.annual_plan_button.click()
        self.locator.continue_user_plan_button.click()


    def website_qr_create(self, temporary_website, qr_code_name):
        self.locator.website_qr_type.click()
        self.locator.setup_website_qr_code_input.fill(temporary_website)
        self.locator.custom_name_qr_code_dropdown.click()
        self.locator.custom_name_qr_code_input(qr_code_type=qr_code_name)
        self.locator.next_button.click()
        self.close_help_modal_window_st3()
        self.locator.create_button.click()




    def close_help_modal_window_st3(self):
        self.locator.help_modal_close_button.is_visible()
        self.locator.help_modal_close_button.click()