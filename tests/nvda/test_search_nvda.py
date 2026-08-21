import pytest
from pages.search import HomePage
from pages.nvda.symbol_page import NvdaSymbolPage
import allure


@pytest.mark.parametrize(
    "query", ["NVDA", "nvda"], ids=["upper", "lower"])
def test_search_via_dropdown(home: HomePage, nvda_page: NvdaSymbolPage, query):
    allure.dynamic.title(f"Поиск через 'dropdown' {query}")
    home.search(query)
    nvda_page.should_be_opened()

@pytest.mark.parametrize("query", ["Nvidia", "nvidia"], ids=["Nvidia", "nvidia"])
def test_search_via_enter(home: HomePage, nvda_page: NvdaSymbolPage, query) -> None:
    allure.dynamic.title(f"Поиск через 'Интер' {query}")
    home.search(query, submit_with_enter=True)
    home.open_first_result(query)
    nvda_page.should_be_opened()

