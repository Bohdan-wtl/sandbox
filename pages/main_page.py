class MainPage:

    def __init__(self, page):
        self.page = page
        self.log_in_button = page.locator("//div[@class='-login-signup']/a[@class='-link-log-in non-draggable']")
        self.sign_up_button = page.locator("//div[@class='-login-signup']/a[@class='-link-sign-up non-draggable']")
        self.main_logo_link = page.locator("//nav[@class='billing-nav']/a")

    def go_to_log_in_page(self):
        self.log_in_button.click()

    def go_to_sign_up_page(self):
        self.sign_up_button.click()
