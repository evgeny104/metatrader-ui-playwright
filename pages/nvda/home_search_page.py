from playwright.sync_api import Locator, expect
from pages.base_page import BasePage
import re


class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_role("searchbox")

    @property
    def first_dropdown_item(self) -> Locator:
        return self.page.locator("div.list a.item").first

    # Actions

    def search(self, query: str, submit_with_enter: bool = False ) -> None:
        """нажимает на кнопку иначе "Enter" -else клик по первой ссылки"""
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            expect(self.first_dropdown_item).to_be_visible()
            self.first_dropdown_item.click()