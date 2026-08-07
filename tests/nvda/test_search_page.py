from playwright.sync_api import expect
import re


def test_search_nvda(page, home):
    """
    Строка поиска на сайте MetaTrader - проверка активного dropdown
    """
    query = "nVda"
    home.search(query)

    expect(page).to_have_url("https://www.metatrader.com/en/symbols/nasdaq/nvda")


def test_search_homepage(page, home):
    """
    Проверяет поиск ввод "Enter" - переход на страницу результатов
    """
    query = "nvda"
    home.search(query, True)

    expect(page.get_by_text(re.compile("NVIDIA", re.IGNORECASE)).first).to_be_visible()

