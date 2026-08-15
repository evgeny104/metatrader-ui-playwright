from pages.nvda.nvda_page import NvdaBasePage
from playwright.sync_api import Locator, expect


class NvdaStatementPage(NvdaBasePage):
    URL = f"{NvdaBasePage.BASE_URL}/statement"

    # Locators

    @property
    def header_row(self) -> Locator:
        return self.page.locator("span.row.header") # достает таблицу с годами

    def year_cell(self, index: int) -> Locator:
        return self.header_row.locator(f'span.cell[data-index="{index}"]')  # достает ячейку с годом по индексу

    @property
    def ttm_cell(self) -> Locator:
        return self.header_row.locator("span.cell.last")  # достает ячейку TTM (последний столбец)

    # Actions

    def should_be_opened(self) -> None:
        super().should_be_opened()  # ← проверяет URL (для test_statement_page.py полиморфизм)
        expect(self.header_row).to_be_visible()  # проверит URL /statement + таблицу