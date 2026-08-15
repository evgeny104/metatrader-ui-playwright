from playwright.sync_api import expect
from pages.nvda.statement_page import NvdaStatementPage
from data.nvda.statement_years import EXPECTED_YEARS


def test_statement_page_opens(nvda_statement_opened: NvdaStatementPage):
    """Проверит URL /statement + таблицу с годами"""
    nvda_statement_opened.should_be_opened()


def test_year_columns_present(nvda_statement_opened: NvdaStatementPage):
    """Проверяет YEARS and TTM в таблице statement"""
    for i, year in enumerate(EXPECTED_YEARS):
        expect(nvda_statement_opened.year_cell(i)).to_have_text(year)

    expect(nvda_statement_opened.ttm_cell).to_have_text("TTM")

