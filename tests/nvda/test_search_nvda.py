from pages.home_search_page import HomePage
from pages.nvda.nvda_symbol_page import NvdaSymbolPage


def test_search_via_dropdown(home: HomePage, nvda_page: NvdaSymbolPage):
    """Ввод 'NVDA' -> клик по первому пункту дропдауна -> страница NVDA"""
    query  = "NVDA"
    home.search(query)
    nvda_page.should_be_opened()


def test_search_lowercase(home: HomePage, nvda_page: NvdaSymbolPage):
    """Поиск в нижнем регистре 'nvda' тоже открывает страницу NVDA"""
    query = "NVDA"
    home.search(query)
    nvda_page.should_be_opened()


def test_search_via_enter(home: HomePage, nvda_page: NvdaSymbolPage):
    """Ввод 'NVIDIA' + Enter -> клик по первому результату -> страница NVDA"""
    query = "NVIDIA"
    home.search(query, submit_with_enter=True)
    home.open_first_result(query)

