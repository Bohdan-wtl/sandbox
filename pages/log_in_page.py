from base.base_page import BasePage


class LogInPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.email_log_in = page.locator("//input[@id='input-email']")
        self.password_log_in = page.locator("//input[@id='input-password']")
        self.log_in_confirm_button = page.locator("//button[@id='login-btn']")

    def log_in(self, temporary_mail, signup_password):
        self.email_log_in.fill(temporary_mail)
        self.log_in_confirm_button.click()
        self.password_log_in.fill(signup_password)
        self.log_in_confirm_button.click()
