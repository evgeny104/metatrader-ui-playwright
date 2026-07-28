import re
from playwright.sync_api import Page, expect

def test_main_page_title(page: Page):
    """Проверка заголовок домашне страницы metatrader.com """
    page.goto("https://www.metatrader.com")
    assert page.title() == "MetaTrader | World Financial Markets for Smarter Trading"


def test_nasdaq_nvda(page: Page):
    """Преходим на страницу NVDA"""
    page.goto("https://www.metatrader.com")
    page.locator('a[href="/en/symbols/nasdaq/nvda"]').first.click()
    assert page.title() == "Nvidia Corp — Chart, Price & News (NASDAQ:NVDA) |  MetaTrader"

def test_nvda_nvda(page: Page):
    page.goto("https://www.metatrader.com")
    page.locator('a[href="/en/symbols/nasdaq/nvda"]').first.click()
    expect(page).to_have_title(re.compile(re.escape("Nvidia Corp — Chart, Price & News (NASDAQ:NVDA) | MetaTrader")))


def test_nasdaq_nvda(page: Page):
    page.goto("https://www.metatrader.com/en/symbols/nasdaq/nvda")
    page.locator('a[href="/en/symbols/nasdaq/nvda/statement"]').first.click()


EXPECTED_YEARS = ["2020","2021", "2022", "2023", "2024", "2025"]


def test_year_columns_present(page: Page):
    page.goto("https://www.metatrader.com/en/symbols/nasdaq/nvda/statement")
    header = page.locator("span.row.header")

    # data-index="1" -> 2021, ..., data-index="5" -> 2025
    for i, year in enumerate(EXPECTED_YEARS, start=0):
        cell = header.locator(f'span.cell[data-index="{i}"]')
        expect(cell).to_have_text(year)

    # плюс TTM в конце
    expect(header.locator("span.cell.last")).to_have_text("TTM")












