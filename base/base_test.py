from pages.admin_web_page import AdminPage
from pages.download_qr_code_page import DownloadPage
from pages.dpf_congratulations_page import DpfCongratsPage
from pages.dpf_flow_download_your_qr_page import DpfDownloadQrPage
from pages.dpf_plans_and_pricing_page import DpfPlansAndPricingPage
from pages.general_plan_and_pricing import GeneralPlansAndPricingPage
from pages.log_in_page import LogInPage
from pages.main_page import MainPage
from pages.menu_page import MenuPage
from pages.my_account_page import MyAccountPage
from pages.my_qr_codes_page import MyQRCodesPage
from pages.payment_page import PaymentPage
from pages.register_page import RegisterPage
from pages.step1_page import Step1Page
from pages.step2_qr_variable_types_page import Step2QrVariable
from pages.step3_qr_design import Step3Page
from pytest import fixture

class BaseTest:
    _admin_web_page = None
    _download_qr_code_page = None
    _dpf_configurations_page = None
    _dpf_flow_download_your_qr_page = None
    _step2_page = None
    _step3_page = None
    _step1_page = None
    _register_page = None
    _payment_page = None
    _my_qr_code_page = None
    _my_account_page = None
    _menu_page = None
    _main_page = None
    _login_page = None
    _general_pricing_page = None
    _dpf_pricing_page = None


    @fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page

    @property
    def admin_web_page(self):
        if self._admin_web_page is None:
            self._admin_web_page = AdminPage(self.page)
        return self._admin_web_page

    @property
    def download_qr_code_page(self):
        if self._download_qr_code_page is None:
            self._download_qr_code_page = DownloadPage(self.page)
        return self._download_qr_code_page

    @property
    def dpf_configurations_page(self):
        if self._dpf_configurations_page is None:
            self._dpf_configurations_page = DpfCongratsPage(self.page)
        return self._dpf_configurations_page

    @property
    def dpf_flow_download_your_qr_page(self):
        if self._dpf_flow_download_your_qr_page is None:
            self._dpf_flow_download_your_qr_page = DpfDownloadQrPage(self.page)
        return self._dpf_flow_download_your_qr_page

    @property
    def step2_page(self):
        if self._step2_page is None:
            self._step2_page = Step2QrVariable(self.page)
        return self._step2_page

    @property
    def step3_page(self):
        if self._step3_page is None:
            self._step3_page = Step3Page(self.page)
        return self._step3_page

    @property
    def step1_page(self):
        if self._step1_page is None:
            self._step1_page = Step1Page(self.page)
        return self._step1_page

    @property
    def register_page(self):
        if self._register_page is None:
            self._register_page = RegisterPage(self.page)
        return self._register_page

    @property
    def payment_page(self):
        if self._payment_page is None:
            self._payment_page = PaymentPage(self.page)
        return self._payment_page

    @property
    def my_qr_code_page(self):
        if self._my_qr_code_page is None:
            self._my_qr_code_page = MyQRCodesPage(self.page)
        return self._my_qr_code_page

    @property
    def my_account_page(self):
        if self._my_account_page is None:
            self._my_account_page = MyAccountPage(self.page)
        return self._my_account_page

    @property
    def menu_page(self):
        if self._menu_page is None:
            self._menu_page = MenuPage(self.page)
        return self._menu_page

    @property
    def main_page(self):
        if self._main_page is None:
            self._main_page = MainPage(self.page)
        return self._main_page

    @property
    def login_page(self):
        if self._login_page is None:
            self._login_page = LogInPage(self.page)
        return self._login_page

    @property
    def general_pricing_page(self):
        if self._general_pricing_page is None:
            self._general_pricing_page = GeneralPlansAndPricingPage(self.page)
        return self._general_pricing_page

    @property
    def dpf_pricing_page(self):
        if self._dpf_pricing_page is None:
            self._dpf_pricing_page = DpfPlansAndPricingPage(self.page)
        return self._dpf_pricing_page