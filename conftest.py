import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage

@pytest.fixture(autouse=True)
def home(page: Page) -> HomePage:
    """Фикстура стартовая страница"""
    return HomePage(page)

@pytest.fixture(autouse=True)
def open_metatrader(page: Page):
    """Фикстура для подготовки окружения теста"""
    page.goto("https://www.metatrader.com/en")
    yield page



@pytest.fixture()
def open_nvda_statement(page: Page):
    """Фикстура для подготовки окружения теста /nvda/statement"""
    page.goto("https://www.metatrader.com/en/symbols/nasdaq/nvda/statement")
    yield page