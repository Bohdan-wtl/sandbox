import random
from base.base_page import BasePage


class Step3Page(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def close_help_modal_window_st3(self):
        self.help_modal_close_button.is_visible()
        self.help_modal_close_button.click()

    def select_random_frame_option(self):
        # A list of qr code frames from which one will be selected randomly.
        design_frame_locators = [
            "//button[@id='qr_frame_id_0']",
            "//button[@id='qr_frame_id_1']",
            "//button[@id='qr_frame_id_2']",
            "//button[@id='qr_frame_id_3']",
            "//button[@id='qr_frame_id_4']",
            "//button[@id='qr_frame_id_5']",
            "//button[@id='qr_frame_id_6']",
            "//button[@id='qr_frame_id_7']",
            "//button[@id='qr_frame_id_8']",
            "//button[@id='qr_frame_id_9']",
            "//button[@id='qr_frame_id_10']",
            "//button[@id='qr_frame_id_11']",
            "//button[@id='qr_frame_id_12']",
            "//button[@id='qr_frame_id_13']",
            "//button[@id='qr_frame_id_14']",
            "//button[@id='qr_frame_id_15']"
        ]
        random_frame = random.choice(design_frame_locators)
        self.page.locator(random_frame).click()
        return random_frame

    def select_frame_step3(self):
        self.frame_step3_dropdown.click()
        self.select_random_frame_option()

    def select_random_qrcode_pattern(self):
        # A list of QR code patterns from which one will be selected randomly.
        pattern_style_locators = [
            "//label[@id='square']",
            "//label[@id='round']",
            "//label[@id='extra_rounded']",
            "//label[@id='dot']",
            "//label[@id='heart']",
            "//label[@id='diamond']"
        ]
        random_pattern = random.choice(pattern_style_locators)
        self.page.locator(random_pattern).click()
        return random_pattern

    def select_pattern_step3(self):
        self.qrcode_patterns_step3_dropdown.click()
        self.select_random_qrcode_pattern()

    def select_random_qrcode_frame_around_corner(self):
        # A list of QR code corners from which one will be selected randomly.
        corner_frame_style_locators = [
            "//label[@id='NS']",
            "//label[@id='FR']",
            "//label[@id='FS']",
            "//label[@id='FRR']",
            "//label[@id='FF']",
            "//label[@id='FL']"
        ]
        random_corner_frame = random.choice(corner_frame_style_locators)
        self.page.locator(random_corner_frame).click()
        return random_corner_frame

    def select_random_qrcode_corner_dot(self):
        # A list of QR code corners from which one will be selected randomly.
        corner_frame_style_locators = [
            "//label[@id='IN']",
            "//label[@id='ID']",
            "//label[@id='IS']",
            "//label[@id='IR']",
            "//label[@id='IDD']",
            "//label[@id='IF']",
            "//label[@id='IL']"
        ]
        random_corner_dot = random.choice(corner_frame_style_locators)
        self.page.locator(random_corner_dot).click()
        return random_corner_dot

    def select_qrcode_corners_step3(self):
        self.qrcode_corners_step3_dropdown.click()
        self.select_random_qrcode_frame_around_corner()
        self.select_random_qrcode_corner_dot()
