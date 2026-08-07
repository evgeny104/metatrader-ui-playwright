from playwright.sync_api import Page, expect
from data.nvda.statement_years import EXPECTED_YEARS


def test_year_columns_present(page: Page, open_nvda_statement):
    header = page.locator("span.row.header")

    # data-index="1" -> 2021, ..., data-index="5" -> 2025
    for i, year in enumerate(EXPECTED_YEARS, start=0):
        cell = header.locator(f'span.cell[data-index="{i}"]')
        expect(cell).to_have_text(year)

    # TTM in end
    expect(header.locator("span.cell.last")).to_have_text("TTM")