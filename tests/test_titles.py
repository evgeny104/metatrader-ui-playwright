from playwright.sync_api import Page

def test_main_page_title(page: Page):
    """Проверка заголовок домашне страницы metatrader.com """
    page.goto("https://www.metatrader.com")
    assert page.title() == "MetaTrader | World Financial Markets for Smarter Trading"

def test_nasdaq_nvda_statment(page: Page):
    page.goto("https://www.metatrader.com/en/symbols/nasdaq/nvda/statement")
    



