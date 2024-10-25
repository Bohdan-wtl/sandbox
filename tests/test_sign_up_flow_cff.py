import pytest
from faker import Faker
from playwright.sync_api import expect
from pages.main_page import (MainPage)
from config import BASE_URL_STAGING
from pages.download_qr_code_page import DownloadPage
from pages.dpf_flow_download_your_qr_page import DpfDownloadQrPage
from pages.step2_qr_variable_types_page import (WebsiteQrType, PdfQrType, LinksQrType, BusinessQrType, ImagesQrType, \
    VideoQrType, AppsQrType, CouponQrType, Mp3QrType, MenuQrType, WiFiQrType, FacebookQrType, VCardQrType,
                                                    InstagramQrType, SocialMediaQrType, WhatsAppQrType)
from utils.generation_test_data import temporary_website

url_dpf = f"{BASE_URL_STAGING}/create?step=1&qr_onboarding=active_dpf"


@pytest.fixture
def navigate_to_dpf_page(page, BASE_URL_STAGING):
    dpf_cff_url = f"{BASE_URL_STAGING}/create?step=1&qr_onboarding=active_dpf"
    page.goto(dpf_cff_url)


@pytest.fixture(scope="function")
def email_cff():
    fake = Faker()
    temporary_mail = "wtl.automation" + fake.aba() + "@test.com"
    return temporary_mail


def test_cff_sign_up_website_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_website = WebsiteQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_website.website_qr_create(temporary_website)
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_pdf_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_pdf = PdfQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_pdf.pdf_qr_create(page)
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_links_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_links = LinksQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_links.links_qr_create(temporary_website)
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_vcard_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_v_card = VCardQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_v_card.vcard_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_business_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_business = BusinessQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_business.business_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_image_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_images = ImagesQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_images.image_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_video_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_video = VideoQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_video.video_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_apps_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_apps = AppsQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_apps.apps_qr_create(temporary_website)
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_coupon_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_coupon = CouponQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_coupon.coupon_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_mp3_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_mp3 = Mp3QrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_mp3.mp3_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_menu_menu_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_menu = MenuQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_menu.menu_menu_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_menu_pdf_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_menu = MenuQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_menu.menu_pdf_qr_create(page)
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_menu_link_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_menu = MenuQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_menu.menu_link_qr_create(temporary_website)
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_wifi_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_wifi = WiFiQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_wifi.wifi_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


# QR types are not available on staging
def test_cff_sign_up_facebook_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_facebook = FacebookQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_facebook.facebook_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_instagram_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_instagram = InstagramQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_instagram.instagram_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_social_media_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_social_media = SocialMediaQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_social_media.social_media_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_cff_sign_up_whatsapp_qr_type(page, navigate_to_dpf_page, email_cff):
    qr_whatsapp = WhatsAppQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    success_image = DownloadPage(page)
    main_page = MainPage(page)

    qr_whatsapp.whatsapp_qr_create()
    dpf_setup_email_page.dpf_form_email_input.fill(email_cff)
    dpf_setup_email_page.dpf_form_submit_button.click()
    main_page.main_logo_link.click()
    expect(success_image.sign_up_success_image).to_be_enabled()
