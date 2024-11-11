import pytest
from base.base_test import BaseTest
from config import languages_urls


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
@pytest.mark.parametrize("language", languages_urls.keys())
class TestDebug(BaseTest):

    def test_website_qr_code_create(self, sign_up_fixture, fake_email):
        self.qr_creation_page.website_qr_create()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()


    def test_pdf_qr_code_create(self, sign_up_fixture, fake_email):
        self.qr_creation_page.pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()