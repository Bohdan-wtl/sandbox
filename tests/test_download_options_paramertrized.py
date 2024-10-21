import pytest
from pages.download_qr_code_page import DownloadPage
from utils.generation_test_data import download_path

formats = ["PNG",
           #"JPEG", "SVG"
           ]
resolutions = [#"Default",
               #"512x512",
               "1024x1024",
               #"2048x2048",
               #"4096x4096"
               ]

format_pdf = ["PDF"]
pdf_size = [#"Default",
            "A4",
            #"A3",
            #"A2",
            #"A1",
            #"A0"
            ]


# Test download "PDF" in all sizes
@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize("file_format", format_pdf)
@pytest.mark.parametrize("resolution", pdf_size)
def test_parametrized_pdf_qr_download_default_sign_up(page, setup_qr_code_creation, file_format, resolution):
    download_qr_code_page = DownloadPage(page)
    my_qr_code_page = setup_qr_code_creation

    my_qr_code_page.download_qr_code_button.is_enabled()
    my_qr_code_page.download_qr_code_button.click()
    download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)


# Test download "PNG", "JPEG", "SVG" formats in all sizes
@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize("file_format", formats)
@pytest.mark.parametrize("resolution", resolutions)
def test_parametrized_img_download_default_sign_up(page, setup_qr_code_creation, file_format, resolution):
    download_qr_code_page = DownloadPage(page)
    my_qr_code_page = setup_qr_code_creation

    my_qr_code_page.download_qr_code_button.is_enabled()
    my_qr_code_page.download_qr_code_button.click()
    download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)


# Test download "PDF" in all sizes
@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize("file_format", format_pdf)
@pytest.mark.parametrize("resolution", pdf_size)
def test_parametrized_pdf_download_dpf_sign_up(page, setup_qr_code_creation_dpf_flow, file_format, resolution):
    download_qr_code_page = DownloadPage(page)
    my_qr_code_page = setup_qr_code_creation_dpf_flow

    my_qr_code_page.download_qr_code_button.click()
    download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)


# Test download "PNG", "JPEG", "SVG" formats in all sizes
@pytest.mark.flaky(reruns=2)
@pytest.mark.parametrize("file_format", formats)
@pytest.mark.parametrize("resolution", resolutions)
def test_parametrized_img_download_dpf_sign_up(page, setup_qr_code_creation_dpf_flow, file_format, resolution):
    download_qr_code_page = DownloadPage(page)
    my_qr_code_page = setup_qr_code_creation_dpf_flow

    my_qr_code_page.download_qr_code_button.is_visible()
    my_qr_code_page.download_qr_code_button.click()
    download_qr_code_page.download_parametrize_files(file_format, resolution, download_path)

