import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from utils.generation_test_data import temporary_website


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestDefaultSignUpFlow(BaseTest):

    def test_website_qr_code_create(self, sign_up_fixture):
        self.website_qr.website_qr_create(temporary_website)
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_pdf_qr_code_create(self, sign_up_fixture):
        self.pdf_qr.pdf_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_links_qr_code_create(self, sign_up_fixture):
        self.links_qr.links_qr_create(temporary_website)
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_vcard_qr_code_create(self, sign_up_fixture):
        self.vcard_qr.vcard_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_business_qr_code_create(self, sign_up_fixture):
        self.business_qr.business_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_images_qr_code_create(self, sign_up_fixture):
        self.images_qr.image_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_video_qr_code_create(self, sign_up_fixture):
        self.video_qr.video_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_apps_qr_code_create(self, sign_up_fixture):
        self.apps_qr.apps_qr_create(temporary_website)
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_coupon_qr_code_create(self, sign_up_fixture):
        self.coupon_qr.coupon_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_mp3_qr_code_create(self, sign_up_fixture):
        self.mp3_qr.mp3_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_menu_qr_code_create_menu_type(self, sign_up_fixture):
        self.menu_qr.menu_menu_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_menu_qr_code_create_pdf_type(self, sign_up_fixture):
        self.menu_qr.menu_pdf_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_menu_qr_code_create_link_type(self, sign_up_fixture):
        self.menu_qr.menu_link_qr_create(temporary_website)
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_wi_fi_qr_code_type(self, sign_up_fixture):
        self.wifi_qr.wifi_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_facebook_qr_code_type(self, sign_up_fixture):
        self.facebook_qr.facebook_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_instagram_qr_code_type(self, sign_up_fixture):
        self.instagram_qr.instagram_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_social_media_qr_code_type(self, sign_up_fixture):
        self.social_media_qr.social_media_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()

    def test_whatsapp_qr_code_type(self, sign_up_fixture):
        self.whatsapp_qr.whatsapp_qr_create()
        expect(self.download_qr_code_page.sign_up_success_image).to_be_enabled()
