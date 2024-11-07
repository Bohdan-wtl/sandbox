import os
import shutil
import allure
import pytest
import requests
from pytest import hookimpl
from playwright.sync_api import sync_playwright
from random import Random
from config import languages_urls, languages_dpf_urls, languages_nsf_urls

headless = False
slow_mo = 0

DELETE_USER_URL = "https://oqg-dev.test-qr.com/api/test-user-delete"


@pytest.fixture(scope="session")
def browser(request):
    with sync_playwright() as p:
        browser = getattr(p, request.param).launch(headless=headless)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(request, browser):
    context = browser.new_context(viewport={"width": 1440, "height": 1080}, record_video_dir="videos/")
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    page.close()
    if request.node.rep_call.failed:
        page.video.save_as(path=f"videos/{request.node.name}.webm")


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def artifacts(request):
    yield
    if request.node.rep_call.failed:
        allure.attach.file(f"screenshots/{request.node.name}.png", name="screenshot",
                           attachment_type=allure.attachment_type.PNG)
        allure.attach.file(f"videos/{request.node.name}.webm", name="video",
                           attachment_type=allure.attachment_type.WEBM)


@pytest.fixture(scope="session", autouse=True)
def clean_folders():
    folders_to_clean = ["generated_files", "downloaded_qr_codes", "reports", "screenshots", "videos", "tests/snapshots"]
    for folder in folders_to_clean:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
    yield


@pytest.fixture(scope='function')
def fake_email():
    random_number = Random().randint(3000, 9999999999999)
    fake_email = f"wtl-automation{random_number}@test.com"
    return fake_email


@pytest.fixture(scope='function')
def sign_up_fixture(request, fake_email, language):
    stage_url = languages_urls[language]
    email = fake_email
    request.instance.main_page.open_page(stage_url)
    request.instance.main_page.go_to_sign_up_page()
    request.instance.register_page.sign_up(email, "wtl-testBohdan@gmail.com")
    yield

@pytest.fixture(scope='function')
def delete_user_after_test(fake_email):
    yield
    headers = {"Content-Type": "application/json"}
    data = {
        "emails": [fake_email]
    }
    response = requests.post(DELETE_USER_URL, headers=headers, json=data)
    if response.status_code == 200:
        print(f"User with email {fake_email} deleted successfully.")
    else:
        print(f"Failed to delete user with email {fake_email}. Status code: {response.status_code}, "
              f"Response: {response.text}")


@pytest.fixture(scope='function')
def navigate_to_dpf_page(request, dpf_language):
    stage_url = languages_dpf_urls[dpf_language]
    request.instance.main_page.open_page(stage_url)

@pytest.fixture(scope='function')
def navigate_to_nsf_page(request, nsf_language):
    stage_url = languages_nsf_urls[nsf_language]
    request.instance.main_page.open_page(stage_url)
