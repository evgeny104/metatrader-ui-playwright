from playwright.sync_api import Locator
from pages.base_page import BasePage
import re


class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_role("searchbox")

    @property
    def search_button(self) -> Locator:
        return self.page.locator(
            "div.text", has_text=re.compile(r"^NVDA \(NASDAQ\): Nvidia Corp$")
        )

    # Actions

    def search(self, query: str, submit_with_enter: bool = False ) -> None:
        """Только вводит текст в поисковую строку."""
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            self.search_button.first.click()