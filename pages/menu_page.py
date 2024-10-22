from  base.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.create_qr_code = page.locator("//ul[@class='app-sidebar-links']/li[1]")
        self.analytics = page.locator("//ul[@class='app-sidebar-links']/li[2]")
        self.my_qr_codes = page.locator("//ul[@class='app-sidebar-links']/li[3]")
        self.my_account = page.locator("//ul[@class='app-sidebar-links']/li[4]")
        self.billing = page.locator("//ul[@class='app-sidebar-links']/li[5]")

    def go_to_my_account(self):
        self.my_account.click()
