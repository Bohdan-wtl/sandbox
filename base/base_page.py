from playwright.sync_api import Page, expect, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect

    def navigate(self, url):
        self.page.goto(url)

    def is_visible(self, locator):
        self.expect(self.page.locator(locator)).to_be_visible()

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def open_in_new_tab(self, locator):
        with self.page.expect_popup() as popup_info:
            locator.click(button="middle")
        new_page = popup_info.value
        return new_page

    def get_url(self):
        return self.page.url

    def title(self):
        return self.page.title()