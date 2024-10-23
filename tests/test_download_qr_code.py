import pytest
from base.base_test import BaseTest
from tests.test_sign_up_flow_default import TestDefaultSignUpFlow
from tests.test_sign_up_flow_dpf import TestDPFSignUpFlow
from utils.generation_test_data import download_path


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestQrCodeDownload(BaseTest):

    # Download DPF flow
    def test_dpf_download_website_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_website_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_pdf_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_pdf_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_links_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_links_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_vcard_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_vcard_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_business_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_business_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_images_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_images_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_video_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_video_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_apps_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_apps_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_coupon_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_coupon_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_mp3_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_mp3_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_menu_menu_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_menu_menu_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_menu_pdf_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_menu_pdf_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_menu_link_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_menu_link_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    def test_dpf_download_wifi_qr_type(self, navigate_to_dpf_page, fake_email):
        dpf_flow = TestDPFSignUpFlow()
        dpf_flow.test_sign_up_wifi_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.file_download(download_path)

    # Download default flow
    def test_default_download_website_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_website_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_pdf_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_pdf_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_links_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_links_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_vcard_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_vcard_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_business_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_business_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_images_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_images_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_video_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_video_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_apps_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_apps_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_coupon_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_coupon_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_mp3_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_mp3_qr_code_create(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_menu_menu_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_menu_qr_code_create_menu_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_menu_pdf_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_menu_qr_code_create_pdf_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_menu_link_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_menu_qr_code_create_link_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_wi_fi_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_wi_fi_qr_code_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    # New QR types dev environment
    def test_default_download_facebook_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_facebook_qr_code_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_instagram_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_instagram_qr_code_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_social_media_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_social_media_qr_code_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)

    def test_default_download_whatsapp_qr_type(self, sign_up_fixture):
        default_flow = TestDefaultSignUpFlow()
        default_flow.test_whatsapp_qr_code_type(sign_up_fixture)
        self.download_qr_code_page.file_download(download_path)
