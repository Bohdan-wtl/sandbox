import pytest
from playwright.sync_api import expect
from pages.download_qr_code_page import DownloadPage
from utils.generation_test_data import temporary_website
from pages.step2_qr_variable_types_page import (WebsiteQrType, PdfQrType, LinksQrType, BusinessQrType, ImagesQrType, \
                                                    VideoQrType, AppsQrType, CouponQrType, Mp3QrType, MenuQrType,
                                                    WiFiQrType, VCardQrType, FacebookQrType,
                                                    InstagramQrType, SocialMediaQrType, WhatsAppQrType)


def log_browser_console(page):
    page.on("console", lambda msg: print(f"Console log: {msg.type}: {msg.text}"))


def test_website_qr_code_create(sign_up_fixture, page):
    log_browser_console(page)
    qr_website = WebsiteQrType(page)
    success_image = DownloadPage(page)

    qr_website.website_qr_create(temporary_website)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_pdf_qr_code_create(sign_up_fixture, page):
    success_image = DownloadPage(page)
    qr_pdf = PdfQrType(page)

    qr_pdf.pdf_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_links_qr_code_create(sign_up_fixture, page):
    success_image = DownloadPage(page)
    qr_links = LinksQrType(page)

    qr_links.links_qr_create(temporary_website)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_vcard_qr_code_create(sign_up_fixture, page):
    success_image = DownloadPage(page)
    qr_v_card = VCardQrType(page)

    qr_v_card.vcard_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_business_qr_code_create(sign_up_fixture, page):
    success_image = DownloadPage(page)
    qr_business = BusinessQrType(page)

    qr_business.business_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_images_qr_code_create(sign_up_fixture, page):
    qr_images = ImagesQrType(page)
    success_image = DownloadPage(page)

    qr_images.image_qr_create(page)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_video_qr_code_create(sign_up_fixture, page):
    qr_video = VideoQrType(page)
    success_image = DownloadPage(page)

    qr_video.video_qr_create(page)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_apps_qr_code_create(sign_up_fixture, page):
    qr_apps = AppsQrType(page)
    success_image = DownloadPage(page)

    qr_apps.apps_qr_create(temporary_website)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_coupon_qr_code_create(sign_up_fixture, page):
    qr_coupon = CouponQrType(page)
    success_image = DownloadPage(page)

    qr_coupon.coupon_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_mp3_qr_code_create(sign_up_fixture, page):
    qr_mp3 = Mp3QrType(page)
    success_image = DownloadPage(page)

    qr_mp3.mp3_qr_create(page)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_menu_qr_code_create_menu_type(sign_up_fixture, page):
    qr_menu = MenuQrType(page)
    success_image = DownloadPage(page)

    qr_menu.menu_menu_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_menu_qr_code_create_pdf_type(sign_up_fixture, page):
    qr_menu = MenuQrType(page)
    success_image = DownloadPage(page)

    qr_menu.menu_pdf_qr_create(page)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_menu_qr_code_create_link_type(sign_up_fixture, page):
    qr_menu = MenuQrType(page)
    success_image = DownloadPage(page)

    qr_menu.menu_link_qr_create(temporary_website)
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_wi_fi_qr_code_type(sign_up_fixture, page):
    qr_wifi = WiFiQrType(page)
    success_image = DownloadPage(page)

    qr_wifi.wifi_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


# QR types are not available on staging
def test_facebook_qr_code_type(sign_up_fixture, page):
    qr_facebook = FacebookQrType(page)
    success_image = DownloadPage(page)

    qr_facebook.facebook_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_instagram_qr_code_type(sign_up_fixture, page):
    qr_instagram = InstagramQrType(page)
    success_image = DownloadPage(page)

    qr_instagram.instagram_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_social_media_qr_code_type(sign_up_fixture, page):
    qr_social_media = SocialMediaQrType(page)
    success_image = DownloadPage(page)

    qr_social_media.social_media_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_whatsapp_qr_code_type(sign_up_fixture, page):
    qr_whatsapp = WhatsAppQrType(page)
    success_image = DownloadPage(page)

    qr_whatsapp.whatsapp_qr_create()
    expect(success_image.sign_up_success_image).to_be_enabled()