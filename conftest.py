import pytest
from playwright.sync_api import Page
from pages.home_search_page import HomePage
from pages.nvda.nvda_symbol_page import NvdaSymbolPage


@pytest.fixture
def home(page: Page) -> HomePage:
    page.goto("https://www.metatrader.com/")
    return HomePage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "locale": "en-US",
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 1000,  # замедление как --slowmo 1000mc
    }

@pytest.fixture
def nvda_page(page: Page) -> NvdaSymbolPage:
    return NvdaSymbolPage(page)