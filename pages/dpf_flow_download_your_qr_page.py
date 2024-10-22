from base.base_page import BasePage


class DpfDownloadQrPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.dpf_form_title = page.locator("//form[@id='register-dpf-form']/div[@class='-form-title']")
        self.dpf_form_email_input = page.locator("//input[@id='input-email']")
        self.dpf_form_submit_button = page.locator("//button[contains(@class,'-btn-submit')]")
