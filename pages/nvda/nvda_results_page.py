from pages.base_page import BasePage
from playwright.sync_api import Locator, expect
import re


class SearchResultsPage(BasePage):

    # Locators

    @ property
    def result_item(self) -> Locator:
        """Ищет элемент с текстом NVIDIA"""

        return self.page.get_by_text(re.compile("NVIDIA", re.IGNORECASE))

    # Actions

    def should_be_opened(self, submit_with_enter: bool = False) -> None:
        """if submit_with_enter -> chek dropdown"""

        if submit_with_enter:
            expect(self.result_item.first).to_be_visible()

        else:
            expect(self.page).to_have_url("https://www.metatrader.com/en/symbols/nasdaq/nvda")
            expect(self.result_item.first).to_be_visible()


