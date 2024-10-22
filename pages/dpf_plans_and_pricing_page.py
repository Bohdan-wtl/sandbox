from base.base_page import BasePage


class DpfPlansAndPricingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.days_14_limited_access_button = page.locator("//input[@id='dpfPlan1']")
        self.days_14_full_access_button = page.locator("//input[@id='dpfPlan2']")
        self.annual_plan_button = page.locator("//input[@id='dpfPlan3']")
        self.continue_user_plan_button = page.locator("//a[@id='user_plan_url']")

    def select_dpf_plan(self):
        self.annual_plan_button.click()
        self.continue_user_plan_button.click()
