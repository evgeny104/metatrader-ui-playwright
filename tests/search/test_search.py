from playwright.sync_api import expect
from pages.search import HomePage


def test_search_input_is_visible(home: HomePage):
    """Поисковая строка видна на главной странице"""
    expect(home.search_input).to_be_visible()


def test_search_opens_with_slash_key(home: HomePage):
    """Нажатие '/' фокусирует поисковую строку"""
    home.page.keyboard.press("/")
    expect(home.search_input).to_be_focused()


def test_search_dropdown_appears(home: HomePage):
    """При вводе тикера появляется выпадающий список - дропдаун"""
    home.search_input.fill("alp")
    expect(home.first_dropdown_item).to_be_visible()


def test_search_by_symbol_prefix(home: HomePage):
    """Поиск с префиксом $symbol -> показывает дропдаун"""
    home.search_input.fill("$NVDA")
    expect(home.first_dropdown_item).to_be_visible()