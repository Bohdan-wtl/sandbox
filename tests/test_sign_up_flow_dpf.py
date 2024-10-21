import pytest
from faker import Faker
from playwright.sync_api import expect
from pages.payment_page import PaymentPage
from pages.download_qr_code_page import DownloadPage
from pages.dpf_congratulations_page import DpfCongratsPage
from pages.dpf_flow_download_your_qr_page import DpfDownloadQrPage
from pages.dpf_plans_and_pricing_page import DpfPlansAndPricingPage
from pages.step2_qr_variable_types_page import (WebsiteQrType, PdfQrType, LinksQrType, BusinessQrType, ImagesQrType, \
    VideoQrType, AppsQrType, CouponQrType, Mp3QrType, MenuQrType, WiFiQrType, FacebookQrType, VCardQrType,
                                                    InstagramQrType, SocialMediaQrType, WhatsAppQrType)
from utils.generation_test_data import temporary_website


def test_sign_up_website_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_website = WebsiteQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)
    success_image = DownloadPage(page)

    qr_website.website_qr_create(temporary_website)
    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_pdf_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_pdf = PdfQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_pdf.pdf_qr_create(page)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_links_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_links = LinksQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_links.links_qr_create(temporary_website)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_vcard_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_v_card = VCardQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_v_card.vcard_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_business_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_business = BusinessQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_business.business_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_images_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_images = ImagesQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_images.image_qr_create(page)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_video_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_video = VideoQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_video.video_qr_create(page)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_apps_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_apps = AppsQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_apps.apps_qr_create(temporary_website)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_coupon_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_coupon = CouponQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_coupon.coupon_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_mp3_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_mp3 = Mp3QrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_mp3.mp3_qr_create(page)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_menu_menu_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_menu = MenuQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_menu.menu_menu_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_menu_pdf_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_menu = MenuQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_menu.menu_pdf_qr_create(page)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_menu_link_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_menu = MenuQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_menu.menu_link_qr_create(temporary_website)

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_wifi_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_wifi = WiFiQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_wifi.wifi_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


# NEW methods - not tested
def test_sign_up_facebook_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_facebook = FacebookQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_facebook.facebook_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_instagram_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_instagram = InstagramQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_instagram.instagram_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_social_media_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_social_media = SocialMediaQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_social_media.social_media_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()


def test_sign_up_whatsapp_qr_type(page, navigate_to_dpf_page, email_dpf):
    qr_whatsapp = WhatsAppQrType(page)
    dpf_setup_email_page = DpfDownloadQrPage(page)
    dpf_pricing = DpfPlansAndPricingPage(page)
    success_image = DownloadPage(page)
    dpf_congrats = DpfCongratsPage(page)
    payment_page = PaymentPage(page)

    qr_whatsapp.whatsapp_qr_create()

    dpf_setup_email_page.dpf_form_email_input.fill(email_dpf)
    dpf_setup_email_page.dpf_form_submit_button.click()
    dpf_pricing.select_dpf_plan()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.click()
    expect(success_image.sign_up_success_image).to_be_enabled()