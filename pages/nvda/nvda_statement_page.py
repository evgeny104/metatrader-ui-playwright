from pages.nvda.nvda_base_page import NvdaBasePage
from playwright.sync_api import Locator, expect


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

    def should_be_opened(self) -> None:
        expect(self.page).to_have_url(self.URL)
        expect(self.header_row).to_be_visible()