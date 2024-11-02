import pytest
from base.base_test import BaseTest


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestFrameComparatives(BaseTest):

    @pytest.fixture(scope='function')
    def log_in_fixture(self):
        self.main_page.open_page("https://oqg-staging.test-qr.com/")
        self.main_page.go_to_log_in_page()
        self.login_page.log_in("wtl-test+897897897@gmail.com", "wtl-test+897897897@gmail.com")
        yield

    def test_make_iframe_screenshot(self, log_in_fixture):
        self.my_qr_codes_page.locator.header_create_qr_code_button.click()
        self.qr_creation_page.locator.vcard_qr_type.click(delay=1000)
        self.qr_creation_page.locator.help_modal_close_button.click()
        self.qr_creation_page.locator.basic_info_company_logo_input.set_input_files("resources/screenshot_1.png")
        self.qr_creation_page.locator.v_card_qr_code_first_name_input.fill("Jhon")
        self.qr_creation_page.locator.v_card_qr_code_last_name_input.fill("Doe")
        self.qr_creation_page.locator.contact_details_qr_code_add_phone_btn.click()
        self.qr_creation_page.locator.contact_details_qr_code_add_phone_label.fill("Mobile")
        self.qr_creation_page.locator.contact_details_qr_code_add_phone_number.fill("123456789")
        self.qr_creation_page.locator.contact_details_qr_code_add_email_btn.click()
        self.qr_creation_page.locator.contact_details_qr_code_add_email_label.fill("Work")
        self.qr_creation_page.locator.contact_details_qr_code_add_email_address.fill("Test@gmail.com")
        self.qr_creation_page.locator.contact_details_qr_code_add_website_btn.click()
        self.qr_creation_page.locator.contact_details_qr_code_add_website_label.fill("Website")
        self.qr_creation_page.locator.contact_details_qr_code_add_website_url.fill("https://www.google.com")
        self.qr_creation_page.page.add_style_tag(content="""
            .card {
                border-radius: 0px !important;
            }
            .mb-frame-inner .card::after {
                background-image: none !important;
            }
            #iframesrc, #iframesrc * {
                border-radius: 0px !important;
            }
        """)

        mobile = self.qr_creation_page.page.locator("//div[@id='tabs-1']/div")
        iphone_line = self.qr_creation_page.page.locator("//div[@class='iphone-line']")
        iphone_line.evaluate("element => element.style.position = 'none'")
        mobile.evaluate("element => element.style.height = '100vh'")
        mobile.evaluate("element => element.style.backgroundImage = 'none'")
        iframe = self.qr_creation_page.page.frame_locator("//iframe[@id='iframesrc']")
        iframe.locator("//div[@class='App']").screenshot(path="frame/test.png")
