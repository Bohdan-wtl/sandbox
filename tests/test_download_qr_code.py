from tests import test_sign_up_flow_dpf
from tests import test_sign_up_flow_default
from pages.download_qr_code_page import DownloadPage
from utils.generation_test_data import download_path


# Download DPF flow

def test_dpf_download_website_qr_type(page, navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_website_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_pdf_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_pdf_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_links_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_links_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_vcard_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_vcard_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_business_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_business_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_images_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_images_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_video_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_video_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_apps_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_apps_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_coupon_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_coupon_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_mp3_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_mp3_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_menu_menu_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_menu_menu_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_menu_pdf_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_menu_pdf_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_menu_link_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_menu_link_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


def test_dpf_download_wifi_qr_type(page,navigate_to_dpf_page, email_dpf):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_dpf.test_sign_up_wifi_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.file_download(download_path)


# Download default flow

def test_default_download_website_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_website_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_pdf_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_pdf_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_links_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_links_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_vcard_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_vcard_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_business_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_business_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_images_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_images_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_video_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_video_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_apps_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_apps_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_coupon_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_coupon_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_mp3_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_mp3_qr_code_create(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_menu_menu_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_menu_qr_code_create_menu_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_menu_pdf_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_menu_qr_code_create_pdf_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_menu_link_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_menu_qr_code_create_link_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_wi_fi_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_wi_fi_qr_code_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


# New QR types dev environment
def test_default_download_facebook_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_facebook_qr_code_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_instagram_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_instagram_qr_code_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_social_media_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_social_media_qr_code_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)


def test_default_download_whatsapp_qr_type(page, sign_up_fixture):
    download_qr_code_page = DownloadPage(page)
    test_sign_up_flow_default.test_whatsapp_qr_code_type(sign_up_fixture, page)
    download_qr_code_page.file_download(download_path)
