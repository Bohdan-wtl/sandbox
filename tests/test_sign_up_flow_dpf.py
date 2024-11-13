import allure
import pytest
from base.base_test import BaseTest
from config import languages_dpf_urls

@pytest.mark.parametrize("dpf_language", languages_dpf_urls.keys())
@allure.feature("DPF sign up flow")
class TestDPFSignUpFlow(BaseTest):

    @allure.title("Website QR type")
    def test_sign_up_website_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.website_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("PDF QR type")
    def test_sign_up_pdf_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Links QR type")
    def test_sign_up_links_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.links_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("VCard QR type")
    def test_sign_up_vcard_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.vcard_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Business QR type")
    def test_sign_up_business_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.business_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Image QR type")
    def test_sign_up_images_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.image_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Video QR type")
    def test_sign_up_video_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.video_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Apps QR type")
    def test_sign_up_apps_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.apps_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Coupon QR type")
    def test_sign_up_coupon_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.coupon_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("MP3 QR type")
    def test_sign_up_mp3_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.mp3_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Menu-Menu QR type")
    def test_sign_up_menu_menu_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.menu_menu_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Menu-PDF QR type")
    def test_sign_up_menu_pdf_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.menu_pdf_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Menu-Link QR type")
    def test_sign_up_menu_link_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.menu_link_qr_create()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("WiFi QR type")
    def test_sign_up_wifi_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.wifi_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Facebook QR type")
    def test_sign_up_facebook_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.facebook_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.locator.submit_payment_button.click()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Instagram QR type")
    def test_sign_up_instagram_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.instagram_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("Social_media QR type")
    def test_sign_up_social_media_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.social_media_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")

    @allure.title("WhatsApp QR type")
    def test_sign_up_whatsapp_qr_type(self, browser, navigate_to_dpf_page, fake_email):
        self.qr_creation_page.whatsapp_qr_create()
        self.qr_creation_page.click_next_button_step2()
        self.qr_creation_page.complete_step_3()
        self.qr_creation_page.locator.dpf_form_email_input.fill(fake_email)
        self.qr_creation_page.locator.dpf_form_submit_button.click()
        self.qr_creation_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.select_country_and_zip_in_payment_frame()
        self.payment_page.click_on_submit_payment_button()
        self.qr_creation_page.locator.congrats_download_button.click()
        self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.sign_up_success_image).to_be_enabled()
        #self.my_qr_codes_page.file_download("downloaded_qr_codes/")
