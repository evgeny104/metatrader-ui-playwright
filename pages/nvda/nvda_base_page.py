import re
from pages.base_page import BasePage
from playwright.sync_api import Locator


class NvdaBasePage(BasePage):
    BASE_URL = "https://www.metatrader.com/en/symbols/nasdaq/nvda"

    @property
    def symbol_heading(self) -> Locator:
        return self.page.get_by_text(re.compile("NVIDIA", re.IGNORECASE)).first

    def nav_tab(self, name: str) -> Locator:
        return self.page.get_by_role("link", name=name)