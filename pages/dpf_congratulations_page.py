

class DpfCongratsPage:
    def __init__(self, page):
        self.congrats_title_h2 = page.locator("//div[@class='thank-you']/h2")
        self.congrats_download_button = page.locator("//div[@class='thank-you']/div[@class='thank-btn-area']/a")