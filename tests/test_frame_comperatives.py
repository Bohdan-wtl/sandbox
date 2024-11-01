import sys
from PIL import Image
import pytest
from base.base_test import BaseTest
from utils.comparison_module import compare_screenshots


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
        test_func = request.node.originalname
        expected_image_path = (f"tests/snapshots/preview/Expected/{test_func}"
                                   f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}][{sys.platform}].png")
        actual_image_path = (f"tests/snapshots/preview/Actual/{test_func}"
                             f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}][{sys.platform}].png")
        diff_image_path =  (f"tests/snapshots/preview/Diff/{test_func}"
                            f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}][{sys.platform}].png")
        self.qr_creation_page.set_screenshot_path(expected_image_path)
        self.my_qr_codes_page.locator.header_create_qr_code_button.click()
        qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
        qr_create_method_func()
        with Image.open(expected_image_path) as img:
            width, height = img.size
        new_page = self.my_qr_codes_page.open_in_new_tab(self.my_qr_codes_page.open_last_qr_link())
        new_page.set_viewport_size({"width": width, "height": height})
        new_page.wait_for_timeout(5000)
        new_page.screenshot(full_page=True, path=actual_image_path)
        compare_screenshots(actual_image_path, expected_image_path, diff_image_path)
