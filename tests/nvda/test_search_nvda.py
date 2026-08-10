from pages.home_search_page import HomePage
from pages.nvda.nvda_symbol_page import NvdaSymbolPage


def test_search_via_dropdown(home: HomePage, nvda_page: NvdaSymbolPage):
    """Ввод 'NVDA' -> клик по первому пункту дропдауна -> страница NVDA"""
    home.search("NVDA")
    nvda_page.should_be_opened()

def test_search_lowercase(home: HomePage, nvda_page: NvdaSymbolPage):
    """Поиск в нижнем регистре 'nvda' тоже открывает страницу NVDA"""
    home.search("nvda")
    nvda_page.should_be_opened()

def test_search_via_enter(home: HomePage, nvda_page: NvdaSymbolPage):
    """Ввод 'NVIDIA' + Enter -> страница результатов -> клик по первому результату -> страница NVDA"""
    home.search("NVIDIA", submit_with_enter=True) # вводит + жмёт Enter
    home.open_first_result()                            # кликает первую ссылку в результатах
    nvda_page.should_be_opened()                        # проверяет что попали на NVDA

