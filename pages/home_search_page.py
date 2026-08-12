from playwright.sync_api import Locator, expect
from pages.base_page import BasePage

class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_role("searchbox")

    @property
    def first_dropdown_item(self) -> Locator:
        return self.page.locator("header form div.list a.item").first

    @property
    def first_result(self) -> Locator:
        return self.page.locator("div.result-content h2 a").first

    # Actions

    def search(self, query: str, submit_with_enter: bool = False) -> None:
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")
        else:
            # ждём пока дропдаун покажет результаты по запросу (не trending статьи)
            expect(
                self.page.locator("header form div.list a.item").filter(has_text=query.upper()).first
            ).to_be_visible(timeout=3000)
            self.first_dropdown_item.click()

    def open_first_result(self) -> None:
        # ссылка результата открывается с target="_blank" — снимаем, чтобы клик остался в текущей вкладке
        self.first_result.evaluate("el => el.removeAttribute('target')")
        self.first_result.click()