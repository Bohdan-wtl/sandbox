import time

import pytest

from base.base_test import BaseTest

@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestSandBox(BaseTest):

    def test_my_code(self):
        self.main_page.open_page()
        time.sleep(5)

    @pytest.mark.parametrize("qr_type", ["URL", "TEXT", "EMAIL", "PHONE", "SMS", "VCARD", "EVENT", "GEO"])
    def test_all_qr_codes_creation(self, qr_type, sign_up):
        if qr_type == "URL":
            self.main_page.create_qr_code_url()
        if qr_type == "TEXT":
            self.main_page.create_qr_code_text()
        assert True
        pass

    def test_image_creation(self):
        # авторизировался
        # выбрал типа
        # заполняй что хочешь
        assert True
        pass