from playwright.sync_api import expect
from pages.nvda.nvda_statement_page import NvdaStatementPage
from data.nvda.statement_years import EXPECTED_YEARS


def test_statement_page_opens(nvda_statement: NvdaStatementPage):
    nvda_statement.should_be_opened()


def test_year_columns_present(nvda_statement: NvdaStatementPage):
    for i, year in enumerate(EXPECTED_YEARS):
        expect(nvda_statement.year_cell(i)).to_have_text(year)

    expect(nvda_statement.ttm_cell).to_have_text("TTM")