from base.base_page import BasePage


class Step1Page(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.step1_breadcrumbs_section_to_verify_page = page.locator("//span[@id='tab1text']")
        self.menu_burger_button = page.locator("//div[@id='openMenu']")
        self.website_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Url']")
        self.pdf_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Pdf']")
        self.links_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Links']")
        self.vcard_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Vcard']")
        self.business_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Business']")
        self.images_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Images']")
        self.video_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Video']")
        self.apps_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='App']")
        self.coupon_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Coupon']")
        self.mp3_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Mp3']")
        self.menu_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Menu']")
        self.wifi_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Wifi']")
        self.facebook_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Facebook']")
        self.instagram_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Instagram']")
        self.social_media_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Social']")
        self.whatsapp_qr_type = page.locator("//div[@id='step1']//div/input[@data-qr_type='Whatsapp']")

        self.cross_close_btn = page.locator("//button[@id='closeBtn']")

    def open_burger_menu(self):
        self.menu_burger_button.click()
