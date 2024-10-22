import pytest
from faker import Faker
from playwright.sync_api import sync_playwright, expect
from datetime import datetime
from pages.download_qr_code_page import DownloadPage
from pages.main_page import MainPage
from pages.my_qr_codes_page import MyQRCodesPage
from pages.register_page import RegisterPage
from pages.step1_page import Step1Page
from utils.generation_test_data import navigate
from tests import test_sign_up_flow_dpf, test_sign_up_flow_default
from config import BASE_URL_DEV
from config import BASE_URL_STAGING
import os
import shutil
from utils.generation_test_data import signup_password


@pytest.fixture(scope="session")
def playwright_instance():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


@pytest.fixture(scope="function")
def browser(playwright_instance):
    browser = get_browser(playwright_instance,  # "firefox"
                          "webkit"
                          #"chrome"
                          )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(viewport={"width": 1440, "height": 1080},
                                  # record_video_dir="videos/"
                                  )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


def get_browser(playwright, browser_name):
    if browser_name == "chrome":
        return playwright.chromium.launch(channel="chrome", headless=True, slow_mo=0)
    elif browser_name == "headless":
        return playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        return playwright.firefox.launch(channel="firefox", headless=False, slow_mo=000)
    elif browser_name == "webkit":
        return playwright.webkit.launch(headless=False, slow_mo=1000)
    else:
        raise ValueError(f"Unknown browser: {browser_name}")


@pytest.fixture(scope="function")
def email_dpf():
    fake = Faker()
    temporary_mail = "wtl.automation" + fake.aba() + "@test.com"
    return temporary_mail


@pytest.fixture
def navigate_to_dpf_page(page, BASE_URL_STAGING):
    url_dpf = f"{BASE_URL_STAGING}/create?step=1&qr_onboarding=active_dpf"
    page.goto(url_dpf)


@pytest.fixture(scope="function")
def sign_up_fixture(page, BASE_URL_STAGING):
    fake = Faker()
    fake_email = "wtl.automation" + fake.aba() + "@test.com"
    main_page = MainPage(page)
    register_page = RegisterPage(page)
    step1_page = Step1Page(page)

    navigate(BASE_URL_STAGING, page)
    main_page.go_to_sign_up_page()
    register_page.sign_up(fake_email, signup_password)
    expect(step1_page.step1_breadcrumbs_section_to_verify_page).to_be_visible()

    return page


@pytest.fixture(scope="function")
def sign_up_fixture_admin_link_generation(page, BASE_URL_STAGING):
    fake = Faker()
    fake_email = "wtl.automation" + fake.aba() + "@test.com"
    main_page = MainPage(page)
    register_page = RegisterPage(page)
    step1_page = Step1Page(page)

    navigate(BASE_URL_STAGING, page)
    main_page.go_to_sign_up_page()
    register_page.sign_up(fake_email, signup_password)
    expect(step1_page.step1_breadcrumbs_section_to_verify_page).to_be_visible()

    return {"page": page, "email": fake_email}


languages_dev = ["bg", "zh-yue",
                 "zh-cn", "hr",
                 "he", "hi",
                 "hu", "id",
                 "ja", "ko",
                 "ms", "no",
                 "pt-br", "ro",
                 "sr", "sk",
                 "sl", "th", "uk"
                 ]

languages_staging = [#"cs", "da",
                     "en",
                     "fi",
                     "fr", "nl",
                     #"de", "it",
                     #"no", "pl",
                     #"pt", "es",
                     #"sv", "tr",
                     ]


@pytest.fixture(scope="session", params=languages_staging)
def language(request):
    return request.param


@pytest.fixture(scope="session", autouse=True)
def clean_folders():
    folders_to_clean = ["downloaded_qr_codes/", "generated_files/", "screenshot/"]
    for folder in folders_to_clean:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
    yield


@pytest.fixture(scope="function", params=[
    test_sign_up_flow_default.test_website_qr_code_create,
    test_sign_up_flow_default.test_pdf_qr_code_create,
    test_sign_up_flow_default.test_links_qr_code_create,
    test_sign_up_flow_default.test_vcard_qr_code_create,
    test_sign_up_flow_default.test_business_qr_code_create,
    test_sign_up_flow_default.test_images_qr_code_create,
    test_sign_up_flow_default.test_video_qr_code_create,
    test_sign_up_flow_default.test_apps_qr_code_create,
    test_sign_up_flow_default.test_coupon_qr_code_create,
    test_sign_up_flow_default.test_mp3_qr_code_create,
    test_sign_up_flow_default.test_menu_qr_code_create_menu_type,
    test_sign_up_flow_default.test_menu_qr_code_create_pdf_type,
    test_sign_up_flow_default.test_menu_qr_code_create_link_type,
    test_sign_up_flow_default.test_wi_fi_qr_code_type,
    test_sign_up_flow_default.test_facebook_qr_code_type,
    test_sign_up_flow_default.test_instagram_qr_code_type,
    test_sign_up_flow_default.test_social_media_qr_code_type,
    test_sign_up_flow_default.test_whatsapp_qr_code_type
])
def setup_qr_code_creation(sign_up_fixture, page, request):
    download_qr_code_page = DownloadPage(page)
    my_qr_code_page = MyQRCodesPage(page)

    method_to_use = request.param
    method_to_use(page, sign_up_fixture)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{timestamp}"

    download_qr_code_page.download_modal_close_button.click(timeout=20000)
    expect(download_qr_code_page.download_modal_close_button).to_be_hidden()
    # page.screenshot(path=f"screenshot/screenshot{file_name}.png", full_page=True)

    return my_qr_code_page


@pytest.fixture(scope="function", params=[
    test_sign_up_flow_dpf.test_sign_up_website_qr_type,
    test_sign_up_flow_dpf.test_sign_up_pdf_qr_type,
    test_sign_up_flow_dpf.test_sign_up_links_qr_type,
    test_sign_up_flow_dpf.test_sign_up_vcard_qr_type,
    test_sign_up_flow_dpf.test_sign_up_business_qr_type,
    test_sign_up_flow_dpf.test_sign_up_images_qr_type,
    test_sign_up_flow_dpf.test_sign_up_video_qr_type,
    test_sign_up_flow_dpf.test_sign_up_apps_qr_type,
    test_sign_up_flow_dpf.test_sign_up_coupon_qr_type,
    test_sign_up_flow_dpf.test_sign_up_mp3_qr_type,
    test_sign_up_flow_dpf.test_sign_up_menu_menu_qr_type,
    test_sign_up_flow_dpf.test_sign_up_menu_pdf_qr_type,
    test_sign_up_flow_dpf.test_sign_up_menu_link_qr_type,
    test_sign_up_flow_dpf.test_sign_up_wifi_qr_type,
    test_sign_up_flow_dpf.test_sign_up_facebook_qr_type,
    test_sign_up_flow_dpf.test_sign_up_instagram_qr_type,
    test_sign_up_flow_dpf.test_sign_up_social_media_qr_type,
    test_sign_up_flow_dpf.test_sign_up_whatsapp_qr_type
])
def setup_qr_code_creation_dpf_flow(page, navigate_to_dpf_page, request, email_dpf):
    download_qr_code_page = DownloadPage(page)
    my_qr_code_page = MyQRCodesPage(page)
    method_to_use = request.param
    method_to_use(page, navigate_to_dpf_page, email_dpf)
    download_qr_code_page.download_modal_close_button.click()
    return my_qr_code_page
