import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from utils.generation_test_data import temporary_website


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestDPFSignUpFlow(BaseTest):



    def test_sign_up_website_qr_type(self, navigate_to_dpf_page, fake_email):
        self.website_qr.website_qr_create(temporary_website)
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_pdf_qr_type(self, navigate_to_dpf_page, fake_email):
        self.pdf_qr.pdf_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_links_qr_type(self, navigate_to_dpf_page, fake_email):
        self.links_qr.links_qr_create(temporary_website)
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_vcard_qr_type(self, navigate_to_dpf_page, fake_email):
        self.vcard_qr.vcard_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_business_qr_type(self, navigate_to_dpf_page, fake_email):
        self.business_qr.business_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_images_qr_type(self, navigate_to_dpf_page, fake_email):
        self.images_qr.image_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_video_qr_type(self, navigate_to_dpf_page, fake_email):
        self.video_qr.video_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_apps_qr_type(self, navigate_to_dpf_page, fake_email):
        self.apps_qr.apps_qr_create(temporary_website)
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_coupon_qr_type(self, navigate_to_dpf_page, fake_email):
        self.coupon_qr.coupon_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_mp3_qr_type(self, navigate_to_dpf_page, fake_email):
        self.mp3_qr.mp3_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_menu_menu_qr_type(self, navigate_to_dpf_page, fake_email):
        self.menu_qr.menu_menu_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_menu_pdf_qr_type(self, navigate_to_dpf_page, fake_email):
        self.menu_qr.menu_pdf_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_menu_link_qr_type(self, navigate_to_dpf_page, fake_email):
        self.menu_qr.menu_link_qr_create(temporary_website)
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_wifi_qr_type(self, navigate_to_dpf_page, fake_email):
        self.wifi_qr.wifi_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_facebook_qr_type(self, navigate_to_dpf_page, fake_email):
        self.facebook_qr.facebook_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button().click()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_instagram_qr_type(self, navigate_to_dpf_page, fake_email):
        self.instagram_qr.instagram_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_social_media_qr_type(self, navigate_to_dpf_page, fake_email):
        self.social_media_qr.social_media_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_sign_up_whatsapp_qr_type(self, navigate_to_dpf_page, fake_email):
        self.whatsapp_qr.whatsapp_qr_create()
        self.dpf_flow_download_your_qr_page.dpf_form_email_input.fill(fake_email)
        self.dpf_flow_download_your_qr_page.dpf_form_submit_button.click()
        self.dpf_pricing_page.select_dpf_plan()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.click()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()
