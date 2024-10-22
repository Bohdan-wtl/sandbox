import time

import pytest
from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.admin_web_page import AdminPage
from pages.dpf_congratulations_page import DpfCongratsPage
from pages.menu_page import MenuPage
from pages.my_account_page import MyAccountPage
from pages.payment_page import PaymentPage
from tests import test_sign_up_flow_default, test_sign_up_flow_dpf
from pages.download_qr_code_page import DownloadPage
from pages.general_plan_and_pricing import GeneralPlansAndPricingPage

link_to_admin = "https://oqg-staging.test-qr.com/helpdesk"
admin_email = "oqg-dev@outlook.com"
admin_password = "12345678"


@pytest.mark.flaky(reruns=2)
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("discount_button_locator", [
    "default_pricing_button",
    "discount_70_promo_button",   # 70% OFF
    "discount_8_99_monthly_button",  # $8.99 Monthly Page
    "discount_50_one_time_button"   # 50$ One time payment page
])
def test_admin_create_uniq_payment_link(page: Page, sign_up_fixture_admin_link_generation, discount_button_locator):
    admin_page = AdminPage(page)
    dpf_congrats = DpfCongratsPage(page)
    download_page = DownloadPage(page)
    menu_page = MenuPage(page)
    my_account = MyAccountPage(page)
    pricing_plan = GeneralPlansAndPricingPage(page)
    payment_page = PaymentPage(page)
    discount_locator = getattr(admin_page, discount_button_locator)
    success_image = DownloadPage(page)
    test_sign_up_flow_default.test_website_qr_code_create(sign_up_fixture_admin_link_generation, page)
    user_email = sign_up_fixture_admin_link_generation["email"]
    download_page.download_modal_close_button.click()
    menu_page.my_account.click()
    my_account.log_out_button.click()
    page.goto(link_to_admin)
    admin_page.admin_email_input.fill(admin_email)
    admin_page.admin_log_in_button.click()
    admin_page.admin_password_input.fill(admin_password)
    admin_page.admin_log_in_button.click()
    admin_page.global_search_input.fill(user_email)
    admin_page.search_button.click()
    admin_page.get_user_menu_dots_button_users_tab(user_email).click()
    admin_page.generate_discount_url_btn.click()
    discount_locator.click()
    admin_page.generate_link_button.click()
    link_text = admin_page.generated_link.inner_text()
    admin_page.pricing_popup_close_button.click()
    admin_page.admin_logout_area.click()
    admin_page.admin_logout_button.click()
    page.goto(link_text)
    pricing_plan.variable_plan_button_universal_locator.first.click(force=True)
    payment_page.billing_full_name_input.fill("John Smit")
    payment_page.billing_address_line1_input.fill("ser John Smit st.")
    payment_page.billing_city_input.fill("LA")
    payment_page.billing_postal_code_input.fill("37800")
    payment_page.billing_info_continue_button.click()
    payment_page.make_payment()
    payment_page.click_on_submit_payment_button()
    dpf_congrats.congrats_download_button.wait_for(state="visible")
    expect(dpf_congrats.congrats_download_button).to_be_visible()


refund_alert_text = "The refund was successfully made."


@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize("refund_button", [
    "full_refund_plan_button_cancel_subscription",
    "full_refund_plan_button_keep_subscription"
])
def test_admin_full_refund_options(page: Page, navigate_to_dpf_page, email_dpf, refund_button):
    admin_page = AdminPage(page)
    download_page = DownloadPage(page)
    menu_page = MenuPage(page)
    my_account = MyAccountPage(page)
    test_sign_up_flow_dpf.test_sign_up_website_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_page.download_modal_close_button.click()
    menu_page.my_account.click()
    my_account.log_out_button.click()
    page.goto(link_to_admin)
    admin_page.admin_email_input.fill(admin_email)
    admin_page.admin_log_in_button.click()
    admin_page.admin_password_input.fill(admin_password)
    admin_page.admin_log_in_button.click()
    admin_page.menu_payments_button.click()
    admin_page.get_user_menu_dots_button_payments_tab(email_dpf).click()
    admin_page.get_user_menu_refund_button_payments_tab(email_dpf).click()
    getattr(admin_page, refund_button).click()
    admin_page.refund_confirm_button_payments_tab.click()
    expect(admin_page.refund_alert_message).to_have_text(refund_alert_text)


@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize("refund_button", [
    "partial_refund_plan_button_cancel_subscription",
    "partial_refund_plan_button_keep_subscription"
])
def test_admin_partial_refund_options(page: Page, navigate_to_dpf_page, email_dpf, refund_button):
    admin_page = AdminPage(page)
    download_page = DownloadPage(page)
    menu_page = MenuPage(page)
    my_account = MyAccountPage(page)
    test_sign_up_flow_dpf.test_sign_up_website_qr_type(page, navigate_to_dpf_page, email_dpf)
    download_page.download_modal_close_button.click()
    menu_page.my_account.click()
    my_account.log_out_button.click()
    page.goto(link_to_admin)
    admin_page.admin_email_input.fill(admin_email)
    admin_page.admin_log_in_button.click()
    admin_page.admin_password_input.fill(admin_password)
    admin_page.admin_log_in_button.click()
    admin_page.menu_payments_button.click()
    admin_page.get_user_menu_dots_button_payments_tab(email_dpf).click()
    admin_page.get_user_menu_refund_button_payments_tab(email_dpf).click()
    getattr(admin_page, refund_button).click()
    admin_page.refund_confirm_button_payments_tab.click()
    admin_page.refund_amount_input_field.fill("2")
    admin_page.refund_amount_input_payment_button.click()
    expect(admin_page.refund_alert_message).to_have_text(refund_alert_text)
