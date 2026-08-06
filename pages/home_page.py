from playwright.sync_api import Locator
from pages.base_page import BasePage

class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:

        return self.page.get_by_role("searchbox")


    # Actions

    def search(self, query: str) -> None:

        self.search_input.fill(query)
