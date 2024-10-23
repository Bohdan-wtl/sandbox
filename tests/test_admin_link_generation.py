import pytest
from playwright.sync_api import expect
from base.base_test import BaseTest
from tests.test_sign_up_flow_default import TestDefaultSignUpFlow
from tests.test_sign_up_flow_dpf import TestDPFSignUpFlow

link_to_admin = "https://oqg-staging.test-qr.com/helpdesk"
admin_email = "oqg-dev@outlook.com"
admin_password = "12345678"
refund_alert_text = "The refund was successfully made."

@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestAdminLinkGeneration(BaseTest):

    @pytest.mark.flaky(reruns=0)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize("discount_button_locator", [
        "default_pricing_button",
    ])
    def test_admin_create_uniq_payment_link(self, sign_up_fixture_admin_link_generation, discount_button_locator):
        discount_locator = getattr(self.admin_web_page, discount_button_locator)
        TestDefaultSignUpFlow.test_website_qr_code_create(sign_up_fixture_admin_link_generation)
        user_email = sign_up_fixture_admin_link_generation["email"]
        self.download_qr_code_page.download_modal_close_button.click()
        self.menu_page.my_account.click()
        self.my_account_page.log_out_button.click()
        self.my_account_page.navigate(link_to_admin)
        self.admin_web_page.admin_email_input.fill(admin_email)
        self.admin_web_page.admin_log_in_button.click()
        self.admin_web_page.admin_password_input.fill(admin_password)
        self.admin_web_page.admin_log_in_button.click()
        self.admin_web_page.global_search_input.fill(user_email)
        self.admin_web_page.search_button.click()
        self.admin_web_page.get_user_menu_dots_button_users_tab(user_email).click()
        self.admin_web_page.generate_discount_url_btn.click()
        discount_locator.click()
        self.admin_web_page.generate_link_button.click()
        link_text = self.admin_web_page.generated_link.inner_text()
        self.admin_web_page.pricing_popup_close_button.click()
        self.admin_web_page.admin_logout_area.click()
        self.admin_web_page.admin_logout_button.click()
        self.base_page.navigate(link_text)
        self.general_pricing_page.variable_plan_button_universal_locator.first.click(force=True)
        self.payment_page.billing_full_name_input.fill("John Smit")
        self.payment_page.billing_address_line1_input.fill("ser John Smit st.")
        self.payment_page.billing_city_input.fill("LA")
        self.payment_page.billing_postal_code_input.fill("37800")
        self.payment_page.billing_info_continue_button.click()
        self.payment_page.make_payment()
        self.payment_page.click_on_submit_payment_button()
        self.dpf_configurations_page.congrats_download_button.wait_for(state="visible")
        expect(self.dpf_configurations_page.congrats_download_button).to_be_visible()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("refund_button", [
        "full_refund_plan_button_cancel_subscription",
        "full_refund_plan_button_keep_subscription"
    ])
    def test_admin_full_refund_options(self, navigate_to_dpf_page, fake_email, refund_button):
        test_flow = TestDPFSignUpFlow()
        test_flow.test_sign_up_website_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.download_modal_close_button.click()
        self.menu_page.my_account.click()
        self.my_account_page.log_out_button.click()
        self.my_account_page.goto(link_to_admin)
        self.admin_web_page.admin_email_input.fill(admin_email)
        self.admin_web_page.admin_log_in_button.click()
        self.admin_web_page.admin_password_input.fill(admin_password)
        self.admin_web_page.admin_log_in_button.click()
        self.admin_web_page.menu_payments_button.click()
        self.admin_web_page.get_user_menu_dots_button_payments_tab(fake_email).click()
        self.admin_web_page.get_user_menu_refund_button_payments_tab(fake_email).click()
        getattr(self.admin_web_page, refund_button).click()
        self.admin_web_page.refund_confirm_button_payments_tab.click()
        expect(self.admin_web_page.refund_alert_message).to_have_text(refund_alert_text)

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("refund_button", [
        "partial_refund_plan_button_cancel_subscription",
        "partial_refund_plan_button_keep_subscription"
    ])
    def test_admin_partial_refund_options(self, navigate_to_dpf_page, fake_email, refund_button):
        test_flow = TestDPFSignUpFlow()
        test_flow.test_sign_up_website_qr_type(navigate_to_dpf_page, fake_email)
        self.download_qr_code_page.download_modal_close_button.click()
        self.menu_page.my_account.click()
        self.my_account_page.log_out_button.click()
        self.my_account_page.goto(link_to_admin)
        self.admin_web_page.admin_email_input.fill(admin_email)
        self.admin_web_page.admin_log_in_button.click()
        self.admin_web_page.admin_password_input.fill(admin_password)
        self.admin_web_page.admin_log_in_button.click()
        self.admin_web_page.menu_payments_button.click()
        self.admin_web_page.get_user_menu_dots_button_payments_tab(fake_email).click()
        self.admin_web_page.get_user_menu_refund_button_payments_tab(fake_email).click()
        getattr(self.admin_web_page, refund_button).click()
        self.admin_web_page.refund_confirm_button_payments_tab.click()
        self.admin_web_page.refund_amount_input_field.fill("2")
        self.admin_web_page.refund_amount_input_payment_button.click()
        expect(self.admin_web_page.refund_alert_message).to_have_text(refund_alert_text)
