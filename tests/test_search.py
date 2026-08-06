from playwright.sync_api import Page, expect
import re

def test_search_nvda(page,home):
    """
    Проверяет поиск через строку поиска на сайте MetaTrader - проверка активного dropdown
    """
    query = "nvda"
    home.search(query)

    page.locator("div.text", has_text=re.compile(r"^NVDA \(NASDAQ\): Nvidia Corp$")).first.click()
    expect(page).to_have_url("https://www.metatrader.com/en/symbols/nasdaq/nvda")

def test_search_homepage(page,home ):
    """
    Проверяет поиск через строку поиска на сайте MetaTrader - переходим на страничку с результатом
    Ищется строго заголовок конкретной новости.
    """

    query = "NVDA"
    home.search(query)
    page.keyboard.press("Enter")

    expect(page.get_by_text(re.compile("NVIDIA", re.IGNORECASE)).first).to_be_visible()




