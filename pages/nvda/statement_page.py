import allure
from playwright.sync_api import Locator, expect
from pages.nvda.nvda_page import NvdaBasePage
from data.nvda.statement_years import EXPECTED_YEARS


class NvdaStatementPage(NvdaBasePage):
    URL = f"{NvdaBasePage.BASE_URL}/statement"

    # Locators

    @property
    def header_row(self) -> Locator:
        return self.page.locator("span.row.header")

    def year_cell(self, index: int) -> Locator:
        return self.header_row.locator(f'span.cell[data-index="{index}"]')

    @property
    def ttm_cell(self) -> Locator:
        return self.header_row.locator("span.cell.last")

    # Actions

    @allure.step("Проверяем страницу Statement NVDA")
    def should_be_opened(self) -> None:
        with allure.step("URL содержит /nasdaq/nvda/statement"):
            if msg := self._assert_url():
                raise AssertionError(msg)
        with allure.step("Таблица с финансовыми данными видна"):
            try:
                expect(self.header_row).to_be_visible()
            except AssertionError:
                raise AssertionError("Таблица с годами не найдена на странице Statement")

    @allure.step("Проверяем годовые колонки в таблице")
    def check_years(self) -> None:
        for i, year in enumerate(EXPECTED_YEARS):
            with allure.step(f"{year}"):
                expect(self.year_cell(i)).to_have_text(year)
        with allure.step("TTM"):
            expect(self.ttm_cell).to_have_text("TTM")