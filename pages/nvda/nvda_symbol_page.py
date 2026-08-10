from pages.nvda.nvda_base_page import NvdaBasePage
from playwright.sync_api import expect


class NvdaSymbolPage(NvdaBasePage):
    URL = NvdaBasePage.BASE_URL

    def should_be_opened(self) -> None:
        expect(self.symbol_heading).to_be_visible()
        expect(self.page).to_have_url(self.URL)