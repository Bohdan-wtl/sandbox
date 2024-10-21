import pytest


@pytest.fixture(scope="session")
def BASE_URL_STAGING(language):
    return f"https://oqg-staging.test-qr.com/{language}"


@pytest.fixture(scope="session")
def BASE_URL_DEV(language):
    return f"https://oqg-dev.test-qr.com/{language}"
