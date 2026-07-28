from playwright.sync_api import Locator
from pages.base_page import BasePage

class SearchResultsPage(BasePage):

    # Locators
    @property
    def results_page(self) ->Locator:

        return self.page.get_by_text("Search Results")

    # Actions