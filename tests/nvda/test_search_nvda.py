import pytest
from pages.search import HomePage
from pages.nvda.symbol_page import NvdaSymbolPage


@pytest.mark.parametrize("query", ["NVDA", "nvda"])
def test_search_via_dropdown(home: HomePage, nvda_page: NvdaSymbolPage, query):
    home.search(query)
    nvda_page.should_be_opened()

@pytest.mark.parametrize("query", ["Nvidia", "nvidia"])
def test_search_via_enter(home: HomePage, nvda_page: NvdaSymbolPage, query) -> None:
    home.search(query, submit_with_enter=True)
    home.open_first_result(query)
    nvda_page.should_be_opened()

