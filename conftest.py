import pytest
from playwright.sync_api import Page
from pages.nvda.home_search_page import HomePage
from pages.nvda.nvda_results_page import SearchResultsPage


@pytest.fixture(autouse=True)
def open_metatrader(page: Page):
    page.goto("https://www.metatrader.com/")
    yield page

@pytest.fixture
def home(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "locale": "en-US",
    }

@pytest.fixture()
def open_nvda_statement(page: Page):
    page.goto("https://www.metatrader.com/en/symbols/nasdaq/nvda/statement")
    yield page

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "slow_mo": 3000,  # замедление как --slowmo 1000mc
    }

@pytest.fixture
def results(page: Page) -> SearchResultsPage:
    return SearchResultsPage(page)