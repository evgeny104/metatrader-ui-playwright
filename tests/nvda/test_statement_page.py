from pages.nvda.statement_page import NvdaStatementPage
import allure


def test_statement_page_opens(nvda_statement: NvdaStatementPage):
    allure.dynamic.title(f"Проверит URL /statement + таблицу с годами")
    nvda_statement.should_be_opened()


def test_year_columns_present(nvda_statement: NvdaStatementPage):
    allure.dynamic.title("Проверяет атрибуты YEARS в таблице statement")
    nvda_statement.check_years()