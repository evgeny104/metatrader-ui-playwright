import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage


@pytest.fixture(autouse=True)
def open_metatrader(page: Page):
    page.goto("https://www.metatrader.com/")
    yield page


@pytest.fixture(autouse=True)
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
        "slow_mo": 1000,  # замедление как --slowmo 1000mc
    }
