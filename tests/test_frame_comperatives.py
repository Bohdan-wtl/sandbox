# from PIL import Image
# from utils.comparison_module import compare_screenshots
# import pytest
# from random import Random
# from faker import Faker
# from base.base_test import BaseTest
# from config import languages_urls
#
#
# @pytest.mark.parametrize("browser", ["chromium"], indirect=True)
# @pytest.mark.parametrize("languages", languages_urls.keys())
# class TestFrameComparatives(BaseTest):
#
#     @pytest.fixture(autouse=True)
#     def setup_faker(self):
#         self.faker = Faker()
#         self.random_number = Random().randint(3000, 99999999)
#         self.fake_email = "wtl-automation" + str(self.random_number) + "@test.com"
#
#     @pytest.fixture(scope='function', autouse=True)
#     def sign_up_fixture(self, languages):
#         stage_url = languages_urls[languages]
#         self.main_page.open_page(stage_url)
#         self.main_page.go_to_sign_up_page()
#         self.register_page.sign_up(self.fake_email, "wtl-testBohdan@gmail.com")
#         yield
#
#     @pytest.mark.parametrize("qr_create_method", ["apps_qr_create",
#                                                   # "coupon_qr_create", "mp3_qr_create", "menu_menu_qr_create",
#                                                   # "menu_pdf_qr_create", "menu_link_qr_create", "wifi_qr_create", "facebook_qr_create",
#                                                   # "instagram_qr_create", "social_media_qr_create", "whatsapp_qr_create", "video_qr_create",
#                                                   # "image_qr_create", "apps_qr_create", "business_qr_create", "vcard_qr_create", "links_qr_create",
#                                                   # "website_qr_create", "pdf_qr_create"
#                                                   ])
#     def test_comparative_preview_and_view(self, sign_up_fixture, browser, request, qr_create_method):
#         test_func = request.node.originalname
#         expected_image_path = (f"tests/snapshots/preview/Expected/{test_func}"
#                                    f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}].png")
#         actual_image_path = (f"tests/snapshots/preview/Actual/{test_func}"
#                              f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}].png")
#         diff_image_path =  (f"tests/snapshots/preview/Diff/{test_func}"
#                             f"[{browser.browser_type.name}-{qr_create_method}-{browser.browser_type.name}].png")
#         self.qr_creation_page.helper.set_screenshot_path(expected_image_path)
#         qr_create_method_func = getattr(self.qr_creation_page, qr_create_method)
#         qr_create_method_func()
#         self.qr_creation_page.locator.close_download_modal_button.click()
#         with Image.open(expected_image_path) as img:
#             width, height = img.size
#         self.my_qr_codes_page.expect(self.my_qr_codes_page.locator.header_create_qr_code_button).to_be_visible()
#         new_page = self.my_qr_codes_page.open_in_new_tab(self.my_qr_codes_page.open_last_qr_link())
#         new_page.set_viewport_size({"width": width, "height": height})
#         new_page.wait_for_timeout(5000)
#         new_page.locator("body").press("ControlOrMeta+.")
#         new_page.screenshot(full_page=True, path=actual_image_path)
#         compare_screenshots(actual_image_path, expected_image_path, diff_image_path)
