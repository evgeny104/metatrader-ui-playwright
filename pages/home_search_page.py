from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_role("searchbox")

    @property
    def first_dropdown_item(self) -> Locator:
        return self.page.locator("div.list a.item").first

    @property
    def first_result(self) -> Locator:
        return self.page.locator("div.result-content h2 a").first

    # Actions

    def search(self, query: str, submit_with_enter: bool = False ) -> None:
        """нажимает на кнопку "Enter" -else клик по первой ссылки"""
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")

        else:
            expect(self.first_dropdown_item).to_be_visible()
            self.first_dropdown_item.click()

    def open_first_result(self) -> None:
        # ссылка результата открывается с target="_blank" — снимаем, чтобы клик остался в текущей вкладке
        self.first_result.evaluate("el => el.removeAttribute('target')")
        self.first_result.click()