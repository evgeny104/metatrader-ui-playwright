import pytest
from playwright.sync_api import Page
from pages.search import HomePage
from pages.nvda.symbol_page import NvdaSymbolPage

@pytest.fixture
def home(page: Page) -> HomePage:
    page.goto("https://www.metatrader.com/")  # открывает главную страницу
    return HomePage(page)  # создает объект страницы и передает браузер

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "locale": "en-US",  # нужен чтобы сайт отдавал английскую версию
    }

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 1500,  # замедление как --slowmo 1000mc
    }

@pytest.fixture
def nvda_page(page: Page) -> NvdaSymbolPage:
    return NvdaSymbolPage(page)  # создает объект страницы NVDA без перехода (переход происходит через поиск)