import pytest
from playwright.sync_api import Page
from pages.nvda.nvda_statement_page import NvdaStatementPage


@pytest.fixture
def nvda_statement(page: Page) -> NvdaStatementPage:
    page.goto(NvdaStatementPage.URL)
    return NvdaStatementPage(page)