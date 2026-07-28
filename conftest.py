import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

@pytest.fixture(autouse=True)
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture(autouse=True)
def open_litres(page: Page):
    page.goto("https://www.metatrader.com/")
    yield page

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Фикстура для браузера, редирект на страницу US"""
    return {
        **browser_context_args,
        "locale": "US",
    }
