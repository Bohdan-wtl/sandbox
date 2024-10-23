import time

import pytest

from base.base_test import BaseTest

@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestSandBox(BaseTest):

    def test_my_code(self):
        self.main_page.open_page()
        self.main_page.go_to_sign_up_page()
        self.register_page.sign_up("wtl-testBohdan30@gmail.com", "wtl-testBohdan@gmail.com")
        self.qr_creation_page.pdf_qr_create("pdf1")