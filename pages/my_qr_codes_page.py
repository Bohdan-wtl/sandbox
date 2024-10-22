from  base.base_page import BasePage


class MyQRCodesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.download_modal_h3_title = page.locator("//div[@id='DownloadModal']//h3")
        self.download_modal_close_button = page.locator("//div[@id='DownloadModal']//button[@type='button']")
        self.download_qr_code_button = page.locator("//div[contains(@class,'position-relative')]/button[@data-target='#DownloadModal']")
