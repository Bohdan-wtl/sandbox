import pytest
from utils.generation_test_data import download_path
from base.base_test import BaseTest

formats = ["PNG"]  # , "JPEG", "SVG"]
resolutions = ["1024x1024"]  # ,"512x512", "2048x2048", "4096x4096"]

format_pdf = ["PDF"]
pdf_size = ["A4"]  # ,["Default", "A3", "A2", "A1", "A0"]


@pytest.mark.parametrize("browser", ["chromium"], indirect=True)
class TestDownloadOptions(BaseTest):

    # Test download "PDF" in all sizes for default sign-up
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("file_format", format_pdf)
    @pytest.mark.parametrize("resolution", pdf_size)
    def test_parametrized_pdf_qr_download_default_sign_up(self, setup_qr_code_creation, file_format, resolution):
        assert setup_qr_code_creation.download_qr_code_button.is_enabled(), "Download button should be enabled"
        setup_qr_code_creation.download_qr_code_button.click()

        self.download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)

    # Test download "PNG", "JPEG", "SVG" formats in all sizes for default sign-up
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("file_format", formats)
    @pytest.mark.parametrize("resolution", resolutions)
    def test_parametrized_img_download_default_sign_up(self, setup_qr_code_creation, file_format, resolution):
        assert setup_qr_code_creation.download_qr_code_button.is_enabled(), "Download button should be enabled"
        setup_qr_code_creation.download_qr_code_button.click()

        self.download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)

    # Test download "PDF" in all sizes for DPF sign-up
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("file_format", format_pdf)
    @pytest.mark.parametrize("resolution", pdf_size)
    def test_parametrized_pdf_download_dpf_sign_up(self, setup_qr_code_creation_dpf_flow, file_format, resolution):
        assert setup_qr_code_creation_dpf_flow.download_qr_code_button.is_enabled(), "Download button should be enabled"
        setup_qr_code_creation_dpf_flow.download_qr_code_button.click()

        self.download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)

    # Test download "PNG", "JPEG", "SVG" formats in all sizes for DPF sign-up
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("file_format", formats)
    @pytest.mark.parametrize("resolution", resolutions)
    def test_parametrized_img_download_dpf_sign_up(self, setup_qr_code_creation_dpf_flow, file_format, resolution):
        assert setup_qr_code_creation_dpf_flow.download_qr_code_button.is_visible(), "Download button should be visible"
        setup_qr_code_creation_dpf_flow.download_qr_code_button.click()

        self.download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)
