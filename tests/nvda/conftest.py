import pytest
import allure
from playwright.sync_api import Page
from pages.nvda.statement_page import NvdaStatementPage
from screenshot_store import _pages


@pytest.fixture
def nvda_statement(page: Page, request) -> NvdaStatementPage:
    _pages[request.node.nodeid] = page
    with allure.step("Открываем страницу Statement NVDA"):
        page.goto(NvdaStatementPage.URL)
    yield NvdaStatementPage(page)
    _pages.pop(request.node.nodeid, None)