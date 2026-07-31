from playwright.sync_api import Page, expect
from data.data_tests import EXPECTED_YEARS
import pytest

def test_search_nvda(page: Page):
    """
    Проверяет поиск NVDA через строку поиска на сайте MetaTrader:
    - в выпадающем списке подсказок появляется пункт с NVIDIA неточной формулировке
    - клик по подсказке ведет на страницу актива /symbols/nasdaq/nvda
    """
    page.get_by_role("searchbox").fill("NVDA")
    expect(page.locator('a[href$="/symbols/nasdaq/nvda"]').first).to_contain_text("Nvidia", ignore_case=True)

    # first in search
    page.locator('a[href$="/symbols/nasdaq/nvda"]').first.click()
    expect(page).to_have_url("https://www.metatrader.com/en/symbols/nasdaq/nvda")

def test_search_homepage(page: Page):
    """
    Проверяет поиск через строку поиска на сайте MetaTrader:
    """
    expect(page).to_have_url("https://www.metatrader.com/")

    search = page.get_by_role("searchbox")
    search.fill("NVDA")
    page.wait_for_timeout(1500)
    search.press("Enter")

    expect(page.get_by_text("NVDA Bullish Continuation Above Resistance")).to_be_visible()


def test_year_columns_present(page: Page, open_nvda_statement):
    header = page.locator("span.row.header")

    # data-index="1" -> 2021, ..., data-index="5" -> 2025
    for i, year in enumerate(EXPECTED_YEARS, start=0):
        cell = header.locator(f'span.cell[data-index="{i}"]')
        expect(cell).to_have_text(year)

    # TTM in end
    expect(header.locator("span.cell.last")).to_have_text("TTM")












