
class RegisterPage:
    def __init__(self, page):
        self.email_input_field = page.locator("//input[@id='input-email']")
        self.password_input_field = page.locator("//input[@id='input-password']")
        self.sign_up_confirm_button = page.locator("//form[@id='register-form']/button[@class='-btn-submit']")

    def sign_up(self, temporary_mail, signup_password):
        self.email_input_field.is_visible()
        self.email_input_field.fill(temporary_mail)
        self.password_input_field.fill(signup_password)
        self.sign_up_confirm_button.click()
