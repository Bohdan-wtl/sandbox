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

        self.back_button = page.locator("//button[@id='cancel']")
        self.next_button = page.locator("//button[@id='temp_next']")
        self.modal_window_step2 = "//div[@id='helpCarousel']"
        self.help_modal_close_button = page.locator("//div[@id='helpCarousel']//button[@id='closeBtn']")
        # QR code name
        self.custom_name_qr_code_dropdown = page.locator("//button[@data-target='#acc_nameOfQrCode']")
        self.custom_name_qr_code_input = page.locator("//input[@id='name']")
        # QR code password
        self.setup_password_qr_code_dropdown = page.locator("//button[@data-target='#acc_password']")
        self.password_checkbox = page.locator("//input[@id='passcheckbox']")
        self.password_qr_code_input_field = page.locator("//input[@id='passwordField']")
        # QR code folder
        self.setup_new_folder_qr_code_dropdown = page.locator("//button[@data-target='#acc_folder']")
        self.select_folder_title_dropdown = page.locator("//input[@id='folder_title']")
        self.create_new_folder_button = page.locator("//button[@id='createFolderBtn']")
        # QR code fonts
        self.update_fonts_qr_code_dropdown = page.locator("//button[@data-target='#acc_nameOfFonts']")
        self.fonts_title_dropdown = page.locator(
            "//div[@id='dropdown_title']/../div/button[@class='drp-icon-btn-open']")
        self.fonts_texts_dropdown = page.locator("//div[@id='dropdown_text']/../div/button[@class='drp-icon-btn-open']")
        # QR code welcome screen
        self.upload_welcome_screen_qr_code_dropdown = page.locator("//button[@data-target='#acc_welcomeScreen']")
        self.upload_welcome_screen_qr_code_input = "//input[@id='screen']"
        # QR code color theme
        self.update_color_theme_qr_code_dropdown = page.locator("//button[@data-target='#acc_Design']")
        # QR code social networks
        self.social_network_qr_code_dropdown = page.locator("//button[@data-target='#acc_social']")
        # Add list of social networks
        self.social_network_url_input = page.locator("//input[@id='socialUrl']")
        self.social_network_text_input = page.locator("//input[@name='social_icon_text[]']")
        # QR code contact details
        self.contact_details_qr_code_dropdown = page.locator("//button[@data-target='#acc_contactInfo']")
        self.contact_details_contact_name = page.locator("//input[@id='contactName']")
        # add phone
        self.contact_details_qr_code_add_phone_btn = page.locator("//button[@data-target='#add_phone-dis']")
        self.contact_details_qr_code_add_phone_label = page.locator("//input[@id='vcard_phoneLabel']")
        self.contact_details_qr_code_add_phone_number = page.locator("//input[@id='vcard_phone']")
        self.contact_details_qr_code_delete_phone_btn = page.locator(
            "//div[@id='phoneBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add email
        self.contact_details_qr_code_add_email_btn = page.locator("//button[@data-target='#add_email-dis']")
        self.contact_details_qr_code_add_email_label = page.locator("//input[@id='vcard_emailLabel']")
        self.contact_details_qr_code_add_email_address = page.locator("//input[@id='vcard_email']")
        self.contact_details_qr_code_delete_email_btn = page.locator(
            "//div[@id='emailBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add website
        self.contact_details_qr_code_add_website_btn = page.locator("//button[@data-target='#add_website-dis']")
        self.contact_details_qr_code_add_website_label = page.locator("//input[@id='vcard_website_title']")
        self.contact_details_qr_code_add_website_url = page.locator("// input[ @id='vcard_website']")
        self.contact_details_qr_code_delete_email_btn = page.locator(
            "//div[@id='websiteBlock']//button[contains(@class,'delete-btn vcard-remove')]")
        # add location
        self.location_qr_code_dropdown = page.locator("//button[@data-target='#add_website-dis']")
        self.location_qr_code_search_address = page.locator("//input[@id='ship-address1']")
        # add button
        self.add_button_with_link = page.locator("//button[@id='add']")
        self.add_button_with_link_name = page.locator("//input[@id='businessButtons']")
        self.add_button_with_link_url = page.locator("//input[@id='businessButtonUrls']")
        # add button2
        self.add_button2_image_with_link = page.locator("//button[@id='add2']")
        self.add_button2_image_text_input = page.locator("//input[@id='button_text']")
        self.add_button2_image_url_input = page.locator("//input[@id='button_url']")

        # opening hours
        self.monday_checkbox = page.locator("//input[@id='checkboxMon']")
        self.monday_time_from = page.locator("//input[@id='Monday_From']")
        self.monday_time_to = page.locator("//input[@id='Monday_To']")



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
        fake = Faker()
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
        self.social_network_url_input.fill(fake.url())
        self.social_network_text_input.fill(fake.text(max_nb_chars=20))
        return random_social_network

    def select_random_fonts_style(self):
        self.update_fonts_qr_code_dropdown.click()
        self.fonts_title_dropdown.scroll_into_view_if_needed()
        self.fonts_title_dropdown.click(force=True)
        self.page.wait_for_selector("//div[@id='dropdown_title']/button", state="attached")
        title_options = self.page.query_selector_all("//div[@id='dropdown_title']/button")
        random_title_font = random.choice(title_options)
        random_title_font.scroll_into_view_if_needed()
        random_title_font.click(force=True)
        self.page.wait_for_timeout(1000)
        self.fonts_texts_dropdown.click()
        text_options = self.page.query_selector_all("//div[@id='dropdown_text']/button")
        random_text_font = random.choice(text_options)
        random_text_font.scroll_into_view_if_needed()
        random_text_font.click(force=True)

    def welcome_screen_set_img(self):
        self.file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'
        self.upload_welcome_screen_qr_code_dropdown.click()
        self.page.locator(self.upload_welcome_screen_qr_code_input).set_input_files(str(self.file_path))

    def contact_information_add_phone_email_web(self):
        fake = Faker()
        self.contact_details_qr_code_add_phone_btn.click()
        self.contact_details_qr_code_add_phone_label.fill(fake.text(max_nb_chars=20))
        self.contact_details_qr_code_add_phone_number.fill(fake.basic_phone_number())
        self.contact_details_qr_code_add_email_btn.click()
        self.contact_details_qr_code_add_email_label.fill(fake.text(max_nb_chars=20))
        self.contact_details_qr_code_add_email_address.fill(fake.email())
        self.contact_details_qr_code_add_website_btn.click()
        self.contact_details_qr_code_add_website_label.fill(fake.text(max_nb_chars=20))
        self.contact_details_qr_code_add_website_url.fill(fake.url())

    def set_location_step2(self):
        fake = Faker()
        self.location_qr_code_search_address.fill(fake.city())
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

    facilities_options_business_qr = ["//input[@id='ficon']", "//input[@id='ficon1']", "//input[@id='ficon2']",
                          "//input[@id='ficon3']", "//input[@id='ficon4']", "//input[@id='ficon5']",
                          "//input[@id='ficon6']", "//input[@id='ficon7']", "//input[@id='ficon8']",
                          "//input[@id='ficon9']", "//input[@id='ficon10']", "//input[@id='ficon11']",
                          "//input[@id='ficon12']", "//input[@id='ficon13']", "//input[@id='ficon14']"]

    menu_allergens_options_menu_digital = ["//input[@value='cereals']", "//input[@value='crustaceans']", "//input[@value='eggs']",
                              "//input[@value='fish']", "//input[@value='peanuts']", "//input[@value='soy']",
                              "//input[@value='milk']", "//input[@value='fruits']", "//input[@value='celery']",
                              "//input[@value='mustard']", "//input[@value='sesame']", "//input[@value='sulfur']",
                              "//input[@value='lupins']", "//input[@value='molluscs']"]

    def select_random_option(self, locators):
        random_locator = random.choice(locators)
        self.page.locator(random_locator).click()
        return random_locator


class WebsiteQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_image()}'

        self.setup_website_qr_code_dropdown = page.locator("//button[@data-target='#acc_nameOfUrl']")
        self.setup_website_qr_code_input = page.locator("//input[@id='url']")

    def website_qr_create(self, temporary_website):
        self.step1_page.website_qr_type.click()
        self.setup_website_qr_code_input.fill(temporary_website)
        self.step2_page.set_custom_qr_code_name(qr_code_type="Website")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class PdfQrType:
    def __init__(self, page):
        self.page = page
        self.generation_test_data = generation_test_data
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.pdf_file_path = Path(os.getcwd()) / f'{generation_test_data.generate_pdf()}'

        self.upload_pdf_qr_type_dropdown = page.locator("//button[@data-target='#acc_nameOfQrPdf']")
        self.upload_pdf_qr_type_button = page.locator("//div[@id='pdf']")
        self.upload_pdf_qr_type_drop_area = page.locator("#pdf")
        self.directly_show_pdf_checkbox = page.locator("//input[@id='direct_pdf']/following-sibling::label")
        self.add_pdf_information_qr_code_dropdown = page.locator("//button[@data-target='#acc_pdfInformation']")
        self.company_pdf_info_input = page.locator("//input[@id='company']")
        self.title_pdf_info_input = page.locator("//input[@id='pdftitle']")
        self.description_pdf_info_input = page.locator("//textarea[@id='description']")
        self.website_pdf_info_input = page.locator("//input[@id='website']")
        self.button_pdf_info_input = page.locator("//input[@id='button']")

    def pdf_qr_create(self):
        fake = Faker()
        self.step1_page.pdf_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(self.page, '#pdf', self.pdf_file_path)

        # self.directly_show_pdf_checkbox.is_editable() # Directly show the PDF file - option
        # self.directly_show_pdf_checkbox.click() # Directly show the PDF file - option

        self.step2_page.select_random_design_option_two_colors()
        self.company_pdf_info_input.fill(fake.company())
        self.title_pdf_info_input.fill(fake.text(max_nb_chars=100))
        self.description_pdf_info_input.fill(fake.text(max_nb_chars=250))
        self.website_pdf_info_input.fill(fake.url())
        self.button_pdf_info_input.fill(fake.word())
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="PDF")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class LinksQrType:
    def __init__(self, page):
        self.page = page
        self.generation_test_data = generation_test_data
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'

        self.basic_info_links_qr_code_dropdown = page.locator("//button[@data-target='#acc_listInfo']")
        self.basic_info_links_qr_code_image_input = page.locator("//input[@id='companyLogo']")
        self.basic_info_links_qr_code_title_input = page.locator("//input[@id='list_title']")
        self.basic_info_links_qr_code_description_input = page.locator("//textarea[@id='list_description']")
        self.list_of_links_qr_code_dropdown = page.locator("//button[@data-target='#acc_link']")
        self.list_of_links_qr_code_delete_button = page.locator("//div[@class='links-delete-wrap']/button")
        self.list_of_links_qr_code_image_input = page.locator("//input[@id='linkImages1']")
        self.list_of_links_qr_code_link_text_input = page.locator("//input[@id='list_text']")
        self.list_of_links_qr_code_link_url_input = page.locator("//input[@id='list_URL']")
        self.links_qr_code_social_network_url_input = page.locator("//input[@id='socialUrl']")
        self.links_qr_code_social_network_text_input = page.locator("//input[@name='social_icon_text[]']")

    def links_qr_create(self, temporary_website):
        fake = Faker()
        self.step1_page.links_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.basic_info_links_qr_code_image_input.set_input_files(str(self.file_path))
        self.basic_info_links_qr_code_title_input.fill(fake.text(max_nb_chars=27))
        self.basic_info_links_qr_code_description_input.fill(fake.text(max_nb_chars=270))
        self.list_of_links_qr_code_link_text_input.fill(fake.text(max_nb_chars=27))
        self.list_of_links_qr_code_link_url_input.fill(temporary_website)
        self.step2_page.select_random_social_network_option()
        self.links_qr_code_social_network_url_input.fill(temporary_website)
        self.links_qr_code_social_network_text_input.fill(fake.text(max_nb_chars=27))
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Links")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class VCardQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

        self.v_card_qr_code_image_input = page.locator("//input[@id='companyLogo']")
        self.v_card_qr_code_first_name_input = page.locator("//input[@id='vcard_first_name']")
        self.v_card_qr_code_last_name_input = page.locator("//input[@id='vcard_last_name']")
        self.v_card_qr_code_company_details_dropdown = page.locator("//button[@data-target='#acc_companyInfo']")
        self.v_card_qr_code_company_details_company_input = page.locator("//input[@id='vcard_company']")
        self.v_card_qr_code_company_details_profession_input = page.locator("//input[@id='vcard_profession']")
        self.v_card_qr_code_company_details_summary_input = page.locator("//textarea[@id='vcard_note']")

    def vcard_qr_create(self):
        fake = Faker()
        self.step1_page.vcard_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.v_card_qr_code_first_name_input.fill(fake.first_name())
        self.v_card_qr_code_last_name_input.fill(fake.last_name())
        self.step2_page.contact_information_add_phone_email_web()
        #self.step2_page.set_location_step2()
        self.v_card_qr_code_company_details_company_input.fill(fake.company())
        self.v_card_qr_code_company_details_profession_input.fill(fake.word())
        self.v_card_qr_code_company_details_summary_input.fill(fake.text(max_nb_chars=250))
        self.step2_page.select_random_social_network_option()
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="vCard")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class BusinessQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

        self.business_info_business_qr_type_image_input = page.locator("//input[@id='companyLogo']")
        self.business_info_business_qr_type_company_input = page.locator("//input[@id='company']")
        self.business_info_business_qr_type_title_input = page.locator("//input[@id='companyTitle']")
        self.business_info_business_qr_type_subtitle_input = page.locator("//input[@id='companySubtitle']")
        self.business_info_business_qr_type_add_button = page.locator("//button[@id='add']")
        self.about_company_business_qr_type_dropdown = page.locator("//textarea[@id='aboutCompany']")
        self.about_company_business_qr_type_textarea = page.locator("//textarea[@id='aboutCompany']")

    def business_qr_create(self):
        fake = Faker()
        self.step1_page.business_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.business_info_business_qr_type_company_input.fill(fake.company())
        self.business_info_business_qr_type_title_input.fill(fake.text(max_nb_chars=20))
        self.business_info_business_qr_type_subtitle_input.fill(fake.text(max_nb_chars=50))
        self.step2_page.add_button_with_link.click()
        self.step2_page.add_button_with_link_name.fill(fake.word())
        self.step2_page.add_button_with_link_url.fill(fake.url())
        self.step2_page.monday_checkbox.check(force=True)
        self.page.evaluate("document.querySelector('#Monday_From').value = '8:00'")
        self.page.evaluate("document.querySelector('#Monday_To').value = '9:00'")
        #self.step2_page.set_location_step2()
        self.step2_page.contact_details_contact_name.fill(fake.name())
        self.step2_page.contact_information_add_phone_email_web()
        self.step2_page.select_random_social_network_option()
        self.about_company_business_qr_type_textarea.fill(fake.text(max_nb_chars=4000))
        self.step2_page.select_random_option(self.step2_page.facilities_options_business_qr)
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Business")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class ImagesQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_image()}'

        self.upload_image_qr_code_dropdown = page.locator("//button[@data-target='#acc_images']")
        self.upload_image_qr_code_button = page.locator("//div[@id='files']")
        self.upload_image_qr_code_drop_area = page.locator("#files")
        self.vertical_image_qr_code_checkbox = page.locator("//input[@id='uploadCheckbox']")
        self.image_information_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.image_information_qr_code_gallery_title_input = page.locator("//input[@id='image_title']")
        self.image_information_qr_code_gallery_description_input = page.locator("//textarea[@id='image_description']")
        self.image_information_qr_code_website_input = page.locator("//input[@id='website']")

    def image_qr_create(self):
        fake = Faker()
        self.step1_page.images_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.generation_test_data.emulate_drag_and_drop(self.page, '#files', self.file_path)
        self.image_information_qr_code_gallery_title_input.fill(fake.text(max_nb_chars=20))
        self.image_information_qr_code_gallery_description_input.fill(fake.text(max_nb_chars=2000))
        self.image_information_qr_code_website_input.fill(fake.url())
        self.step2_page.add_button2_image_with_link.click()
        self.step2_page.add_button2_image_text_input.fill(fake.word())
        self.step2_page.add_button2_image_url_input.fill(fake.url())
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Image")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class VideoQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_mp4()}'

        self.upload_video_qr_code_dropdown = page.locator("//button[@data-target='#acc_videoUpload']")
        self.upload_video_qr_code_url_input = page.locator("//input[@id='youTubeUrl']")
        self.upload_video_qr_code_button = page.locator("//div[@id='files']//button")
        self.upload_video_qr_code_drop_area = page.locator("#files")
        self.video_show_directly_qr_code_checkbox = page.locator("//input[@id='direct_video']")
        self.video_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_contactInfo']")
        self.video_info_qr_code_company_input = page.locator("//input[@id='companyName']")
        self.video_info_qr_code_video_title_input = page.locator("//input[@id='videoTitle']")
        self.video_info_qr_code_video_description_input = page.locator("//textarea[@id='videoDescription']")

    def video_qr_create(self):
        fake = Faker()
        self.step1_page.video_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(self.page, '#files', self.file_path)
        self.step2_page.select_random_design_option_two_colors()
        self.video_info_qr_code_company_input.fill(fake.company())
        self.video_info_qr_code_video_title_input.fill(fake.text(max_nb_chars=30))
        self.video_info_qr_code_video_description_input.fill(fake.text(max_nb_chars=2000))
        self.step2_page.add_button2_image_with_link.click()
        self.step2_page.add_button2_image_text_input.fill(fake.word())
        self.step2_page.add_button2_image_url_input.fill(fake.url())
        self.step2_page.social_network_qr_code_dropdown.click()
        self.step2_page.select_random_social_network_option()
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Video")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class AppsQrType:
    def __init__(self, page):
        self.file_path = None
        self.page = page
        self.generation_test_data = generation_test_data
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'

        self.app_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.app_info_qr_code_app_name_input = page.locator("//input[@id='app_title']")
        self.app_info_qr_code_dev_company_input = page.locator("//input[@id='app_company']")
        self.app_info_qr_code_logo_img_input = page.locator("//input[@id='companyLogo']")
        self.app_info_qr_code_description_input = page.locator("//textarea[@id='app_description']")
        self.app_info_qr_code_website_input = page.locator("//input[@id='app_website']")
        self.links_to_platforms_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.links_to_platforms_qr_code_google_add_button = page.locator("//button[contains(@class,'google_btn')]")
        self.links_to_platforms_qr_code_google_input = page.locator("//input[@id='google']")
        self.links_to_platforms_qr_code_apple_add_button = page.locator("//button[contains(@class,'apple_btn')]")
        self.links_to_platforms_qr_code_apple_input = page.locator("//input[@id='apple']")
        self.links_to_platforms_qr_code_amazon_add_button = page.locator("//button[contains(@class,'amazone_btn')]")
        self.links_to_platforms_qr_code_amazon_input = page.locator("//input[@id='amazon']")

    def apps_qr_create(self, temporary_website):
        fake = Faker()
        self.step1_page.apps_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.app_info_qr_code_app_name_input.fill('App name')
        self.app_info_qr_code_dev_company_input.fill(fake.company())
        self.app_info_qr_code_logo_img_input.set_input_files(str(self.file_path))
        self.app_info_qr_code_description_input.fill(fake.text(max_nb_chars=2000))
        self.app_info_qr_code_website_input.fill(fake.url())

        self.links_to_platforms_qr_code_google_add_button.click()
        self.links_to_platforms_qr_code_google_input.fill(temporary_website)
        self.links_to_platforms_qr_code_apple_add_button.click()
        self.links_to_platforms_qr_code_apple_input.fill(temporary_website)
        self.links_to_platforms_qr_code_amazon_add_button.click()
        self.links_to_platforms_qr_code_amazon_input.fill(temporary_website)
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="App")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class CouponQrType:
    def __init__(self, page):
        self.page = page
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

        self.offer_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_imageInfo']")
        self.offer_info_qr_code_img_input = page.locator("//input[@id='companyLogo']")
        self.offer_info_qr_code_company_input = page.locator("//input[@id='company']")
        self.offer_info_qr_code_title_input = page.locator("//input[@id='title']")
        self.offer_info_qr_code_description_input = page.locator("//textarea[@id='description']")
        self.offer_info_qr_code_badge_input = page.locator("//input[@id='salesBadge']")
        self.offer_info_qr_code_see_code_button = page.locator("//input[@id='buttonToSeeCode']")
        self.coupon_info_qr_code_dropdown = page.locator("//button[@data-target='#acc_couponInfo']")
        self.coupon_info_qr_code_barcode_toggle = page.locator("//input[@id='couponTgl']")
        self.coupon_info_qr_code_code_input = page.locator("//input[@id='couponCode']")
        self.coupon_info_qr_code_terms_input = page.locator("//textarea[@id='terms']")
        self.coupon_info_qr_code_button_input = page.locator("//input[@id='buttonText']")
        self.coupon_info_qr_code_website_input = page.locator("//input[@id='buttonUrl']")

    def coupon_qr_create(self):
        fake = Faker()
        self.step1_page.coupon_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.offer_info_qr_code_img_input.set_input_files(str(self.file_path))
        self.offer_info_qr_code_company_input.fill(fake.company())
        self.offer_info_qr_code_title_input.fill(fake.text(max_nb_chars=20))
        self.offer_info_qr_code_description_input.fill(fake.text(max_nb_chars=1000))
        self.offer_info_qr_code_badge_input.fill(fake.word())
        self.offer_info_qr_code_see_code_button.fill(fake.word())
        self.coupon_info_qr_code_code_input.fill('5859083434')
        self.coupon_info_qr_code_terms_input.fill(fake.text(max_nb_chars=2000))
        self.coupon_info_qr_code_button_input.fill(fake.word())
        self.coupon_info_qr_code_website_input.fill(fake.url())
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Coupon")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class Mp3QrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_mp3()}'
        self.image_file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'

        self.mp3_upload_dropdown = page.locator("//button[@data-target='#acc_nameOfMp3']")
        self.mp3_upload_add_option_checkbox = page.locator("//input[@id='addDownloadOption']")
        self.mp3_info_img_input = page.locator("//input[@id='companyLogo']")
        self.mp3_info_title_input = page.locator("//input[@id='mp3_title']")
        self.mp3_info_description_input = page.locator("//textarea[@id='mp3_description']")
        self.mp3_info_website_input = page.locator("//input[@id='mp3_website']")
        self.mp3_info_add_button = page.locator("//div[@id='btn-item']")
        self.mp3_info_button_text_input = page.locator("//input[@id='button_text']")
        self.mp3_info_button_website_input = page.locator("//input[@id='button_url']")
        self.mp3_info_button_remove_button = page.locator("//div[@id='add-btn']//button[contains(@class,'removeBtn')]")

    def mp3_qr_create(self):
        fake = Faker()
        self.step1_page.mp3_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(self.page, '#mp3', self.file_path)
        self.step2_page.select_random_design_option_two_colors()
        self.mp3_info_img_input.set_input_files(str(self.image_file_path))
        self.mp3_info_title_input.fill(fake.text(max_nb_chars=20))
        self.mp3_info_description_input.fill(fake.text(max_nb_chars=2000))
        self.mp3_info_website_input.fill(fake.url())
        self.step2_page.add_button_with_link.click()
        self.step2_page.add_button2_image_text_input.fill(fake.word())
        self.step2_page.add_button2_image_url_input.fill(fake.url())
        self.step2_page.social_network_qr_code_dropdown.click()
        self.step2_page.select_random_social_network_option()
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="mp3")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class MenuQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.pdf_qr_type = PdfQrType(page)
        self.website_qr_type = WebsiteQrType(page)
        self.generation_test_data = generation_test_data
        self.image_file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'
        self.pdf_file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_pdf()}'

        self.menu_var_popup_modal_title = page.locator("//div[@id='helpCarousel1']//h5")
        self.menu_var_popup_menu_type_button = page.locator("//div[@id='menuModal']//button[@value='menu']")
        self.menu_var_popup_pdf_type_button = page.locator("//div[@id='menuModal']//button[@value='pdf']")
        self.menu_var_popup_link_type_button = page.locator("//div[@id='menuModal']//button[@value='url']")
        self.menu_var_popup_cross_button = page.locator("//div[@id='menuModal']//button[@value='url']")
        self.menu_menu_type_restaurant_dropdown = page.locator("//button[@data-target='#acc_menuInfo']")
        self.menu_menu_type_restaurant_img_input = page.locator("//input[@id='companyLogo']")
        self.menu_menu_type_restaurant_name_input = page.locator("//input[@id='companyTitle']")
        self.menu_menu_type_restaurant_description_input = page.locator("//textarea[@id='companyDescription']")
        self.menu_menu_type_menu_dropdown = page.locator("//button[@data-target='#acc_product']")
        self.menu_menu_type_section1_dropdown = page.locator(
            "//div[@id='add_section']//button[contains(@class,'section-btn') and @data-target='#menu_section_1']")
        self.menu_menu_type_section1_name_input = page.locator("//input[@id='sectionNames']")
        self.menu_menu_type_section1_description_of_section_input = page.locator("//input[@id='sectionDescriptions']")
        self.menu_menu_type_section1_image_input = page.locator("//input[@id='productImages1']")
        self.menu_menu_type_section1_product_name_input = page.locator(
            "//div[@class='row']//input[contains(@name,'productNames') and contains(@class,'pName')]")
        self.menu_menu_type_section1_name_translated_input = page.locator("//input[@id='productNamesTranslated']")
        self.menu_menu_type_section1_description_input = page.locator("//input[@id='productDescriptions']")
        self.menu_menu_type_section1_price_input = page.locator("//input[@id='productPrices']")
        # add allergens
        self.menu_link_type_url_input = page.locator("//input[@id='url']")

    def menu_menu_qr_create(self):
        fake = Faker()
        self.step1_page.menu_qr_type.click()
        self.menu_var_popup_menu_type_button.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.menu_menu_type_restaurant_img_input.set_input_files(str(self.image_file_path))
        self.menu_menu_type_restaurant_name_input.fill(fake.company())
        self.menu_menu_type_restaurant_description_input.fill(fake.text(max_nb_chars=2000))
        self.menu_menu_type_section1_name_input.fill(fake.word())
        self.menu_menu_type_section1_description_of_section_input.fill(fake.text(max_nb_chars=4000))
        self.menu_menu_type_section1_image_input.set_input_files(str(self.image_file_path))
        self.menu_menu_type_section1_product_name_input.fill(fake.word())
        self.menu_menu_type_section1_name_translated_input.fill(fake.word())
        self.menu_menu_type_section1_description_input.fill(fake.text(max_nb_chars=1000))
        self.menu_menu_type_section1_price_input.fill(str(fake.random_int(min=2, max=100)))
        self.step2_page.select_random_option(self.step2_page.menu_allergens_options_menu_digital)
        self.page.evaluate("document.querySelector('#Monday_From').value = '8:00'")
        self.page.evaluate("document.querySelector('#Monday_To').value = '9:00'")
        self.step2_page.contact_information_add_phone_email_web()
        self.step2_page.select_random_social_network_option()
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Menu - digital")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()

    def menu_pdf_qr_create(self):
        fake = Faker()
        self.step1_page.menu_qr_type.click()
        self.menu_var_popup_pdf_type_button.click()
        self.step2_page.close_help_modal_window_st2()
        self.generation_test_data.emulate_drag_and_drop(self.page, '#pdf', self.pdf_file_path)

        # self.directly_show_pdf_checkbox.is_editable() # Directly show the PDF file - option
        # self.directly_show_pdf_checkbox.click() # Directly show the PDF file - option

        self.step2_page.select_random_design_option_two_colors()
        self.pdf_qr_type.company_pdf_info_input.fill(fake.company())
        self.pdf_qr_type.title_pdf_info_input.fill(fake.text(max_nb_chars=100))
        self.pdf_qr_type.description_pdf_info_input.fill(fake.text(max_nb_chars=250))
        self.pdf_qr_type.website_pdf_info_input.fill(fake.url())
        self.pdf_qr_type.button_pdf_info_input.fill(fake.word())
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Menu - PDF")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()

    def menu_link_qr_create(self, temporary_website):
        self.step1_page.menu_qr_type.click()
        self.menu_var_popup_link_type_button.click()
        self.website_qr_type.setup_website_qr_code_input.fill(temporary_website)
        self.step2_page.set_custom_qr_code_name(qr_code_type="Menu - Website")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class WiFiQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

        self.wi_fi_info_dropdown = page.locator("//button[@data-target='#acc_WiFi_Information']")
        self.wi_fi_info_network_name_input = page.locator("//input[@id='wifi_ssid']")
        self.wi_fi_info_network_password_input = page.locator("//input[@id='wifi_password']")
        self.wi_fi_info_encrypting_type_dropdown = page.locator("//select[@id='wifi_encryption']")

    def wifi_qr_create(self):
        fake = Faker()
        self.step1_page.wifi_qr_type.click()
        self.wi_fi_info_network_name_input.fill(fake.text(max_nb_chars=20))
        self.wi_fi_info_network_password_input.fill(str(fake.text(max_nb_chars=8)))
        random_encryption_type = random.choice(["WPA", "WEP", "WPA/WPA2", "nopass"])
        self.wi_fi_info_encrypting_type_dropdown.select_option(random_encryption_type)
        self.step2_page.set_custom_qr_code_name(qr_code_type="Wi-Fi")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class FacebookQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.image_file_path = Path(os.getcwd()) / f'{self.generation_test_data.generate_image()}'

        self.facebook_design_dropdown = page.locator("//button[@data-target='#facebook-bg']")
        self.facebook_design_image0 = page.locator("//div[@id='facebook-bg']//div[@data-image_id='0']")
        self.facebook_design_image1 = page.locator("//div[@id='facebook-bg']//div[@data-image_id='1']")
        self.facebook_design_image2 = page.locator("//div[@id='facebook-bg']//div[@data-image_id='2']")
        self.facebook_design_background_input = page.locator("//input[@id='fbBgImage']")
        self.facebook_profile_img_dropdown = page.locator("//button[@data-target='#facebook-profile']")
        self.facebook_profile_img_input = page.locator("//input[@id='companyLogo']")
        self.facebook_basic_info_dropdown = page.locator("//button[@data-target='#facebook-details']")
        self.facebook_basic_info_facebook_url = page.locator("//input[@id='facebook_url']")
        self.facebook_basic_info_facebook_title = page.locator("//input[@id='facebook_title']")
        self.facebook_basic_info_facebook_description = page.locator("//textarea[@id='facebook_description']")

    def facebook_qr_create(self):
        fake = Faker()
        self.step1_page.facebook_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.facebook_design_background_input.set_input_files(str(self.image_file_path))
        self.facebook_profile_img_input.set_input_files(str(self.image_file_path))
        self.facebook_basic_info_facebook_url.fill(f"https://www.facebook.com/{fake.word()}")
        self.facebook_basic_info_facebook_title.fill(fake.text(max_nb_chars=35))
        self.facebook_basic_info_facebook_description.fill(fake.text(max_nb_chars=1000))
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Facebook")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class InstagramQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

        self.instagram_basic_info_dropdown = page.locator("//button[@data-target='#instagram_username']")
        self.instagram_basic_info_username_input = page.locator("//input[@id='inst_username']")

    def instagram_qr_create(self):
        fake = Faker()
        self.step1_page.instagram_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.instagram_basic_info_username_input.fill(fake.user_name())
        self.step2_page.set_custom_qr_code_name(qr_code_type="Instagram")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class SocialMediaQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)
        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)
        self.generation_test_data = generation_test_data
        self.file_path = Path(os.getcwd()) / f'{generation_test_data.generate_image()}'

        self.social_media_design_dropdown = page.locator("//button[@data-target='#acc_Design']")
        self.social_media_basic_info_dropdown = page.locator("//button[@data-target='#social-media']")
        self.social_media_basic_info_title = page.locator("//input[@id='social_title']")
        self.social_media_basic_info_description = page.locator("//textarea[@id='social_description']")
        self.social_media_basic_info_description = page.locator("//textarea[@id='social_description']")

    def social_media_qr_create(self):
        fake = Faker()
        self.step1_page.social_media_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.step2_page.select_random_design_option_two_colors()
        self.social_media_basic_info_title.fill(fake.text(max_nb_chars=30))
        self.social_media_basic_info_description.fill(fake.text(max_nb_chars=3000))
        self.generation_test_data.emulate_drag_and_drop(self.page, '#files', self.file_path)
        self.step2_page.select_random_social_network_option()
        self.step2_page.select_random_fonts_style()
        self.step2_page.welcome_screen_set_img()
        self.step2_page.set_custom_qr_code_name(qr_code_type="Social Network")
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()


class WhatsAppQrType:
    def __init__(self, page):
        self.page = page
        self.step1_page = Step1Page(page)

        self.step2_page = Step2QrVariable(page)
        self.step3_page = Step3Page(page)

        self.whats_app_information_dropdown = page.locator("//button[@data-target='#whatsapp_no']")
        self.whats_app_information_phone_input = page.locator("//input[@id='phone']")
        self.whats_app_information_message_input = page.locator("//textarea[@id='whatsapp_body']")

    def whatsapp_qr_create(self):
        self.step1_page.whatsapp_qr_type.click()
        self.step2_page.close_help_modal_window_st2()
        self.whats_app_information_phone_input.fill("0501234567")
        time.sleep(2)
        self.step2_page.next_button.click()
        self.step3_page.close_help_modal_window_st3()
        self.step3_page.select_frame_step3()
        self.step3_page.select_pattern_step3()
        self.step3_page.select_qrcode_corners_step3()
        self.step3_page.qr_logo_set_img()
        self.step3_page.create_button.click()
