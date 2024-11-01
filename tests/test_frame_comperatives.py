import os
import sys
from PIL import Image
import pytest
from pathlib import Path
from base.base_test import BaseTest


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestFrameComparatives(BaseTest):

    @pytest.fixture(scope='function')
    def log_in_fixture(self):
        self.main_page.open_page("https://oqg-staging.test-qr.com/")
        self.main_page.go_to_log_in_page()
        self.login_page.log_in("wtl-test+897@gmail.com", "wtl-test+897@gmail.com")
        yield

    @pytest.mark.parametrize("qr_create_method", ["pdf_qr_create"])
    def test_make_iframe_screenshot_pdf_test(self, log_in_fixture, browser, request, assert_snapshot, qr_create_method):
        test_file = Path(str(request.node.fspath)).stem
        test_func = request.node.originalname
        preview_screenshot_path = (f"tests/snapshots/preview/{test_file}/{test_func}/{test_func}"
                                   f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}][{sys.platform}].png")
        self.qr_creation_page.set_screenshot_path(preview_screenshot_path)
        self.my_qr_codes_page.locator.header_create_qr_code_button.click()
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        with Image.open(preview_screenshot_path) as img:
            width, height = img.size
        new_page = self.my_qr_codes_page.open_in_new_tab(self.my_qr_codes_page.open_last_qr_link())
        new_page.set_viewport_size({"width": width, "height": height})
        new_page.wait_for_timeout(5000)
        diff_image_name = (f"tests/snapshots/webview/{test_file}/{test_func}/{test_func}"
                           f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}][{sys.platform}].png")
        new_page.screenshot(full_page=True, path=diff_image_name)
