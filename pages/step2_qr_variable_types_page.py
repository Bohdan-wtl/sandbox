import os
import time
from pathlib import Path
import random
from base.base_page import BasePage

from faker import Faker
from pages.step1_page import Step1Page
from utils import generation_test_data
from pages.step3_qr_design import Step3Page


class Step2QrVariable(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.file_path = None
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data


    def set_custom_qr_code_name(self, qr_code_type):
        fake = Faker()
        self.custom_name_qr_code_dropdown.click()
        custom_qr_code_name = self.custom_name_qr_code_input.fill(
            f"{qr_code_type}_{str(fake.random_number(digits=9, fix_len=True))}")
        return custom_qr_code_name

    def close_help_modal_window_st2(self):
        self.help_modal_close_button.is_visible()
        self.help_modal_close_button.click()
        self.page.wait_for_selector(self.modal_window_step2, state="hidden", timeout=5000)

    # Design option PDF, vCard, Business, mp3, App, Coupon
    def select_random_design_option_two_colors(self):
        # A list of color designs that will be used randomly one of them
        design_color_style_locators = [
            "//div[@id='formcolorPalette1']",
            "//div[@id='formcolorPalette2']",
            "//div[@id='formcolorPalette4']",
            "//div[@id='formcolorPalette5']",
            "//div[@id='formcolorPalette6']",
            "//div[@id='formcolorPalette7']"
        ]
        random_design = random.choice(design_color_style_locators)
        self.page.locator(random_design).click()
        return random_design

    def select_random_design_option_three_colors(self):
        # A list of color designs that will be used randomly one of them
        design_color_style_locators = [
            "//div[@id='formcolorPalette1']",
            "//div[@id='formcolorPalette2']",
            "//div[@id='formcolorPalette4']",
            "//div[@id='formcolorPalette5']",
            "//div[@id='formcolorPalette6']",
            "//div[@id='formcolorPalette7']"
        ]
        random_design = random.choice(design_color_style_locators)
        self.page.locator(random_design).click()
        return random_design

    def select_random_social_network_option(self):
        # A list of social networks that will be used randomly one of them
        social_networks_locators = [
            "//button[@id='socialicon_id_web']",
            "//button[@id='socialicon_id_dribbble']",
            "//button[@id='socialicon_id_facebook']",
            "//button[@id='socialicon_id_flickr']",
            "//button[@id='socialicon_id_gitHub']",
            "//button[@id='socialicon_id_GitLab']",
            "//button[@id='socialicon_id_Google Review']",
            "//button[@id='socialicon_id_line']",
            "//button[@id='socialicon_id_linkedIn']",
            "//button[@id='socialicon_id_pinterest']",
            "//button[@id='socialicon_id_reddit']",
            "//button[@id='socialicon_id_skype']",
            "//button[@id='socialicon_id_snapchat']",
            "//button[@id='socialicon_id_tripAdvisor']",
            "//button[@id='socialicon_id_tumblr']",
            "//button[@id='socialicon_id_X']",
            "//button[@id='socialicon_id_vimeo']",
            "//button[@id='socialicon_id_vkontakte']",
            "//button[@id='socialicon_id_xing']",
            "//button[@id='socialicon_id_YouTube']",
            "//button[@id='socialicon_id_instagram']",
            "//button[@id='socialicon_id_TikTok']",
            "//button[@id='socialicon_id_WhatsApp']",
            "//button[@id='socialicon_id_telegram']",
            "//button[@id='socialicon_id_Facebook Messenger']",
            "//button[@id='socialicon_id_yelp']",
            "//button[@id='socialicon_id_Uber Eats']",
            "//button[@id='socialicon_id_postmates']",
            "//button[@id='socialicon_id_OpenTable']",
            "//button[@id='socialicon_id_spotify']",
            "//button[@id='socialicon_id_SoundCloud']",
            "//button[@id='socialicon_id_Apple Music']",
            "//button[@id='socialicon_id_OnlyFans']",
            "//button[@id='socialicon_id_DoorDash']",
            "//button[@id='socialicon_id_trustpilot']",
            "//button[@id='socialicon_id_signal']",
            "//button[@id='socialicon_id_WeChat']"
        ]
        random_social_network = random.choice(social_networks_locators)
        self.page.locator(random_social_network).click()
        return random_social_network

    def fonts_style_select(self, page):
        self.update_fonts_qr_code_dropdown.click()
        self.fonts_title_dropdown.scroll_into_view_if_needed()
        self.fonts_title_dropdown.click(force=True)
        self.page.wait_for_selector("//div[@id='dropdown_title']/button", state="attached")
        title_options = page.query_selector_all("//div[@id='dropdown_title']/button")
        random_title_font = random.choice(title_options)
        random_title_font.scroll_into_view_if_needed()
        random_title_font.click(force=True)
        page.wait_for_timeout(1000)
        self.fonts_texts_dropdown.click()
        text_options = page.query_selector_all("//div[@id='dropdown_text']/button")
        random_text_font = random.choice(text_options)
        random_text_font.scroll_into_view_if_needed()
        random_text_font.click(force=True)

    def welcome_screen_set_img(self, page):
        self.file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'
        self.upload_welcome_screen_qr_code_dropdown.click()
        page.locator(self.upload_welcome_screen_qr_code_input).set_input_files(str(self.file_path))


class WebsiteQrType(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)


    def website_qr_create(self, temporary_website):
        time.sleep(1)
        # self.step1_page.website_qr_type.is_editable()
        self.step1_page.website_qr_type.click()
        self.setup_website_qr_code_input.fill(temporary_website)

        self.step2_page.set_custom_qr_code_name(qr_code_type="Website")
        self.step2_page.next_button.click()

        self.step3_page.close_help_modal_window_st3()
        #
        self.step3_page.create_button.click()


class PdfQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.generation_test_data = generation_test_data
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_pdf()}'

    def pdf_qr_create(self):
        fake = Faker()

        self.step1_page.pdf_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(self.page, '#pdf', self.file_path)

        # self.directly_show_pdf_checkbox.is_editable() # Directly show the PDF file - option
        # self.directly_show_pdf_checkbox.click() # Directly show the PDF file - option

        self.step2_page.select_random_design_option_two_colors()
        self.company_pdf_info_input.fill(fake.company())
        self.title_pdf_info_input.fill(fake.text(max_nb_chars=100))
        self.description_pdf_info_input.fill(fake.text(max_nb_chars=250))
        self.website_pdf_info_input.fill(fake.url())
        self.button_pdf_info_input.fill(fake.word())
        self.step2_page.fonts_style_select(self.page)

        self.step2_page.welcome_screen_set_img(self.page)

        self.step2_page.set_custom_qr_code_name(qr_code_type="PDF")
        self.step2_page.next_button.click()

        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()

        self.step3_page.qrcode_add_logo_step3_dropdown.click()
        self.page.locator(self.step3_page.qrcode_upload_logo_input).set_input_files(str(self.file_path))
        self.step3_page.create_button.click()


class LinksQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.generation_test_data = generation_test_data
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_image()}'



    def links_qr_create(self, temporary_website):
        fake = Faker()
        self.step1_page.links_qr_type.click()

        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()

        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'
        self.page.locator(self.basic_info_links_qr_code_image_input).set_input_files(str(self.file_path))

        self.basic_info_links_qr_code_title_input.fill(fake.text(max_nb_chars=27))
        self.basic_info_links_qr_code_description_input.fill(fake.text(max_nb_chars=270))
        self.list_of_links_qr_code_link_text_input.fill(fake.text(max_nb_chars=27))
        self.list_of_links_qr_code_link_url_input.fill(temporary_website)

        self.step2_page.select_random_social_network_option()
        self.links_qr_code_social_network_url_input.fill(temporary_website)
        self.links_qr_code_social_network_text_input.fill(fake.text(max_nb_chars=27))
        self.step2_page.fonts_style_select(self.page)
        self.step2_page.welcome_screen_set_img(self.page)
        self.step2_page.set_custom_qr_code_name(qr_code_type="Links")
        self.step2_page.next_button.click()

        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()

        self.step3_page.qrcode_add_logo_step3_dropdown.click()
        self.page.locator(self.step3_page.qrcode_upload_logo_input).set_input_files(str(self.file_path))
        self.step3_page.create_button.click()


class VCardQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)


    def vcard_qr_create(self):
        fake = Faker()
        self.step1_page.vcard_qr_type.click()

        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.v_card_qr_code_first_name_input.fill(fake.first_name())
        self.v_card_qr_code_last_name_input.fill(fake.last_name())
        self.step2_page.next_button.click()

        self.step3_page.close_help_modal_window_st3()

        self.step3_page.create_button.click()


class BusinessQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def business_qr_create(self):
        self.step1_page.business_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.business_info_business_qr_type_company_input.fill('Some First name')
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class ImagesQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_image()}'



    def image_qr_create(self, page):
        self.step1_page.images_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(page, '#files', self.file_path)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class VideoQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_mp4()}'



    def video_qr_create(self, page):
        self.step1_page.video_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(page, '#files', self.file_path)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class AppsQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def apps_qr_create(self, temporary_website):
        self.step1_page.apps_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.app_info_qr_code_app_name_input.fill('App name')
        self.links_to_platforms_qr_code_google_add_button.click()
        self.links_to_platforms_qr_code_google_input.fill(temporary_website)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class CouponQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def coupon_qr_create(self):
        self.step1_page.coupon_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.coupon_info_qr_code_code_input.fill('5859083434')
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class Mp3QrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_mp3()}'



    def mp3_qr_create(self, page):
        self.step1_page.mp3_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(page, '#mp3', self.file_path)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class MenuQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.file_path = None
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data



    def menu_menu_qr_create(self):
        self.step1_page.menu_qr_type.click()
        self.menu_var_popup_menu_type_button.click()
        self.step2_page.close_help_modal_window_st2()
        self.menu_menu_type_section1_name_input.fill("section name")
        self.menu_menu_type_section1_product_name_input.fill("menu name")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()

    def menu_pdf_qr_create(self, page):
        self.step1_page.menu_qr_type.click()
        self.menu_var_popup_pdf_type_button.click()
        self.step2_page.close_help_modal_window_st2()
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_pdf()}'
        self.generation_test_data.emulate_drag_and_drop(page, '#pdf', self.file_path)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()

    def menu_link_qr_create(self, temporary_website):
        self.step1_page.menu_qr_type.click()
        self.menu_var_popup_link_type_button.click()
        self.menu_link_type_url_input.fill(temporary_website)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class WiFiQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def wifi_qr_create(self):
        self.step1_page.wifi_qr_type.click()
        self.wi_fi_info_network_name_input.fill("Some wifi name")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class FacebookQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def facebook_qr_create(self):
        self.step1_page.facebook_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.facebook_basic_info_facebook_url.fill("https://www.facebook.com/automation_test_example")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class InstagramQrType:
    def __init__(self, page):
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def instagram_qr_create(self):
        self.step1_page.instagram_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.instagram_basic_info_username_input.fill("insta_nickname")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class SocialMediaQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)



    def social_media_qr_create(self):
        self.step1_page.social_media_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.social_media_basic_info_title.fill("social_media_title")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()


class WhatsAppQrType(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

    def whatsapp_qr_create(self):
        self.step1_page.whatsapp_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.whats_app_information_phone_input.fill("0501234567")
        time.sleep(2)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.create_button.click()
