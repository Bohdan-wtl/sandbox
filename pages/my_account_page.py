from  base.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.my_account_name = page.locator("//input[@id='name']")
        self.my_account_surname = page.locator("//input[@id='surname']")
        self.my_account_email = page.locator("//div[@class='input-field-area']/input[@id='email']")
        self.my_account_telephone = page.locator("//input[@id='telephone']")
        self.personal_info_submit_button = page.locator("//button[@id='sbmt']")
        self.password_update_input = page.locator("//input[@id='password']")
        self.password_update_confirm_input = page.locator("//input[@id='re_password']")
        self.password_update_submit_button = page.locator("//button[@id='passSave']")
        self.language_update = page.locator("//select[@id='language']")
        self.language_update_button = page.locator("//button[@id='LangSave']")
        self.log_out_button = page.locator("//span[@class='icon-sign-out']/parent::a")

    def log_out_from_active_session(self):
        self.log_out_button.click()

    def password_update(self, signup_password):
        self.password_update_input.fill(signup_password)
        self.password_update_confirm_input.fill(signup_password)
        self.password_update_submit_button.click()
