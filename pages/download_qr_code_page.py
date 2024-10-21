import os
from datetime import datetime


class DownloadPage:
    def __init__(self, page):
        self.page = page
        self.download_button = page.locator("//div[@class='dl-modal-footer-buttons']/button")
        self.png_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='PNG']")
        self.jpeg_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='JPEG']")
        self.svg_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='SVG']']")
        self.pdf_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='PDF']']")
        self.eps_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='EPS']']")
        self.print_file_download = page.locator("//div[contains(@class,'dl-modal-option-card')]//h6[text()='Print']']")
        self.size_of_qr_file_download_dropdown = page.locator("//div[contains(@class,'dl-modal-size-picker')]/span[contains(@class,'icon-arrow-down')]")
        self.size_default_of_qr_file_download = page.locator("//input[@id='Default']")
        self.size_512_of_qr_file_download = page.locator("//input[@id='512x512']")
        self.size_1024_of_qr_file_download = page.locator("//input[@id='1024x1024']")
        self.size_2048_of_qr_file_download = page.locator("//input[@id='2048x2048']")
        self.size_4096_of_qr_file_download = page.locator("//input[@id='4096x4096']")
        self.download_modal_close_button = page.locator("//div[@id='DownloadModal']//button[@type='button']")
        self.sign_up_success_image = page.locator("//img[contains(@class,'dl-modal-head-img')]")

    def file_download(self, download_path):
        with self.page.expect_download() as download_info:
            self.download_button.click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{timestamp}_{download.suggested_filename}"
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"


    def download_parametrize_files(self, file_format, resolution, download_path):
        format_selector = f"//div[contains(@class,'dl-modal-option-card')]//h6[text()='{file_format}']"
        self.page.locator(format_selector).click()
        self.size_of_qr_file_download_dropdown.click(force=True)
        resolution_selector = f"//input[@id='{resolution}']"
        self.page.locator(resolution_selector).click()
        with self.page.expect_download() as download_info:
            self.download_button.click()
        download = download_info.value
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{file_format}_{resolution}_{timestamp}_{download.suggested_filename}"
        file_path = os.path.join(download_path, file_name)
        download.save_as(file_path)
        assert os.path.exists(file_path), "QR code not downloaded"
