from faker import Faker
from base.base_page import BasePage
from pages.locators.qr_creation_flow_locators import QrCreationLocators
from pages.qr_code_helper import QrCodeHelper


class QrCreationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locator = QrCreationLocators(page)
        self.faker = Faker()
        self.helper = QrCodeHelper(self.page, self.locator)

    # DPF Flow with select_dpf_plan function
    def select_dpf_plan(self):
        self.locator.annual_plan_button.click()
        self.locator.continue_user_plan_button.click()

    def pdf_qr_create(self):
        self.locator.pdf_qr_type.click()
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#dropzone', 'pdf')
        self.helper.select_random_colors()
        self.locator.company_pdf_info_input.fill(self.faker.company())
        self.locator.title_pdf_info_input.fill(self.faker.text(max_nb_chars=100))
        self.locator.description_pdf_info_input.fill(self.faker.text(max_nb_chars=250))
        self.locator.website_pdf_info_input.fill(self.faker.url())
        self.locator.button_pdf_info_input.fill(self.faker.word())
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="PDF")
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.helper.select_pattern_step3()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.emulate_drag_and_drop(self.locator.qrcode_upload_logo_input, 'image')
        self.locator.create_button.click()

    def coupon_qr_create(self):
        self.locator.coupon_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для купонов
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.locator.coupon_info_qr_code_code_input.fill('5859083434')  # Шаг 3: Вводим код купона
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def mp3_qr_create(self):
        self.locator.mp3_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для MP3
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.helper.emulate_drag_and_drop('#mp3', 'mp3')  # Шаг 3: Генерируем и загружаем MP3 через drag-and-drop
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def menu_menu_qr_create(self):
        self.locator.menu_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для меню
        self.locator.menu_var_popup_menu_type_button.click()  # Шаг 2: Выбираем тип меню
        self.helper.close_help_modal_window_st2()  # Шаг 3: Закрываем модальное окно
        self.locator.menu_menu_type_section1_name_input.fill("section name")  # Шаг 4: Заполняем название секции
        self.locator.menu_menu_type_section1_product_name_input.fill("menu name")  # Шаг 5: Заполняем название меню
        self.locator.next_button.click()  # Шаг 6: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 7: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 8: Завершаем создание QR-кода

    def menu_pdf_qr_create(self):
        self.locator.menu_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для меню (PDF)
        self.locator.menu_var_popup_pdf_type_button.click()  # Шаг 2: Выбираем PDF тип меню
        self.helper.close_help_modal_window_st2()  # Шаг 3: Закрываем модальное окно
        self.helper.emulate_drag_and_drop('#pdf', 'pdf')  # Шаг 4: Генерируем и загружаем PDF через drag-and-drop
        self.locator.next_button.click()  # Шаг 5: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 6: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 7: Завершаем создание QR-кода

    def menu_link_qr_create(self):
        self.locator.menu_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для меню (ссылка)
        self.locator.menu_var_popup_link_type_button.click()  # Шаг 2: Выбираем тип меню (ссылка)
        self.locator.menu_link_type_url_input.fill(self.faker.url())  # Шаг 3: Вводим временный URL
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def wifi_qr_create(self):
        self.locator.wifi_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для Wi-Fi
        self.locator.wi_fi_info_network_name_input.fill("Some wifi name")  # Шаг 2: Вводим имя Wi-Fi сети
        self.locator.next_button.click()  # Шаг 3: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 4: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 5: Завершаем создание QR-кода

    def facebook_qr_create(self):
        self.locator.facebook_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для Facebook
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.locator.facebook_basic_info_facebook_url.fill(
            "https://www.facebook.com/automation_test_example")  # Шаг 3: Заполняем URL Facebook
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def instagram_qr_create(self):
        self.locator.instagram_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для Instagram
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.locator.instagram_basic_info_username_input.fill(
            "insta_nickname")  # Шаг 3: Вводим имя пользователя Instagram
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def social_media_qr_create(self):
        self.locator.social_media_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для социальных сетей
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.locator.social_media_basic_info_title.fill(
            "social_media_title")  # Шаг 3: Заполняем название профиля социальных сетей
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def whatsapp_qr_create(self):
        self.locator.whatsapp_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для WhatsApp
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.locator.whats_app_information_phone_input.fill("0501234567")  # Шаг 3: Вводим номер телефона для WhatsApp
        self.locator.next_button.click()  # Шаг 5: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 6: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 7: Завершаем создание QR-кода

    def video_qr_create(self):
        self.locator.video_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для видео
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.helper.emulate_drag_and_drop('#files', 'mp4')  # Шаг 3: Генерируем и загружаем видео через drag-and-drop
        self.locator.next_button.click()  # Шаг 4: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 5: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 6: Завершаем создание QR-кода

    def image_qr_create(self):
        self.locator.images_qr_type.click()
        self.helper.close_help_modal_window_st2()
        self.helper.emulate_drag_and_drop('#dropzone', 'image')
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click()

    def apps_qr_create(self):
        self.locator.apps_qr_type.click()  # Шаг 1: Нажимаем на тип QR-кода для приложений
        self.helper.close_help_modal_window_st2()  # Шаг 2: Закрываем модальное окно
        self.locator.app_info_qr_code_app_name_input.fill('App name')  # Шаг 3: Заполняем имя приложения
        self.locator.links_to_platforms_qr_code_google_add_button.click()  # Шаг 4: Добавляем ссылку на Google платформу
        self.locator.links_to_platforms_qr_code_google_input.fill(self.faker.url())  # Шаг 5: Заполняем URL приложения
        self.locator.next_button.click()  # Шаг 6: Переходим к следующему шагу
        self.helper.close_help_modal_window_st3()  # Шаг 7: Закрываем следующее модальное окно
        self.locator.create_button.click()  # Шаг 8: Завершаем создание QR-кода

    def business_qr_create(self):
        self.locator.business_qr_type.click()
        self.helper.close_help_modal_window_st2()
        self.locator.business_info_business_qr_type_company_input.fill('Some First name')
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click()

    def vcard_qr_create(self):
        self.locator.vcard_qr_type.click()
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_colors()
        self.locator.v_card_qr_code_first_name_input.fill(self.faker.first_name())
        self.locator.v_card_qr_code_last_name_input.fill(self.faker.last_name())
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click()

    def links_qr_create(self):
        self.locator.links_qr_type.click()
        self.helper.close_help_modal_window_st2()
        self.helper.select_random_colors()
        self.helper.emulate_drag_and_drop(self.locator.basic_info_links_qr_code_image_input, 'image')
        self.locator.basic_info_links_qr_code_title_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.basic_info_links_qr_code_description_input.fill(self.faker.text(max_nb_chars=270))
        self.locator.list_of_links_qr_code_link_text_input.fill(self.faker.text(max_nb_chars=27))
        self.locator.list_of_links_qr_code_link_url_input.fill(self.faker.url())
        self.helper.select_random_social_network_option()
        self.locator.links_qr_code_social_network_url_input.fill(self.faker.url())
        self.locator.links_qr_code_social_network_text_input.fill(self.faker.text(max_nb_chars=27))
        self.helper.fonts_style_select()
        self.helper.welcome_screen_set_img()
        self.helper.set_custom_qr_code_name(qr_code_type="Links")
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.helper.select_frame_step3()
        self.helper.select_pattern_step3()
        self.helper.select_qrcode_corners_step3()
        self.locator.qrcode_add_logo_step3_dropdown.click()
        self.helper.emulate_drag_and_drop(self.locator.qrcode_upload_logo_input, 'image')
        self.locator.create_button.click()

    def website_qr_create(self):
        self.locator.website_qr_type.click()
        self.locator.setup_website_qr_code_input.fill(self.faker.url())
        self.locator.custom_name_qr_code_dropdown.click()
        self.locator.custom_name_qr_code_input(qr_code_type="Website")
        self.locator.next_button.click()
        self.helper.close_help_modal_window_st3()
        self.locator.create_button.click()
