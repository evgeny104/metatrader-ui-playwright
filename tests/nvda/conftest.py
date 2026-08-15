import pytest
from playwright.sync_api import Page
from pages.nvda.statement_page import NvdaStatementPage

@pytest.fixture
def nvda_statement_opened(page: Page) -> NvdaStatementPage:
    """тест начинается со страницы Statement Nvidia"""
    page.goto(NvdaStatementPage.URL)
    return NvdaStatementPage(page)