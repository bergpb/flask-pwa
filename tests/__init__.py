import pytest

from sample_app import app


@pytest.fixture()
def client():
    context = app.app_context()
    context.push()

    yield app.test_client()

    context.pop()
    return app


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options
