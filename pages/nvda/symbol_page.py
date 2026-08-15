from pages.nvda.nvda_page import NvdaBasePage
from playwright.sync_api import expect


class NvdaSymbolPage(NvdaBasePage):
    URL = NvdaBasePage.BASE_URL  # URL страницы символа NVDA

    # Actions
    def should_be_opened(self) -> None:
        """проверит URL /nvda + заголовок NVIDIA"""
        super().should_be_opened()
        expect(self.symbol_heading).to_be_visible()
