from playwright.sync_api import Locator, expect
from pages.base_page import BasePage
import re

class HomePage(BasePage):

    # Locators

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_role("searchbox")  # достает поле ввода поиска в хедере

    @property
    def first_dropdown_item(self) -> Locator:
        return self.page.locator("header form div.list a.item").first  # достает первый элемент дропдауна

    @property
    def first_result(self) -> Locator:
        return self.page.locator("div.result-content h2 a").first  # достает первую ссылку на странице по поиску

    # Actions

    def search(self, query: str, submit_with_enter: bool = False) -> None:
        self.search_input.fill(query)

        if submit_with_enter:
            self.page.keyboard.press("Enter")  # переходит на /en/search?keyword=QUERY
        else:
            # ждём пока дропдаун покажет результаты по запросу (не trending статьи)
            expect(
                self.page.locator("header form div.list a.item").filter(has_text=query.upper()).first
            ).to_be_visible(timeout=3000)
            self.first_dropdown_item.click()  # кликает по нужному символу в дропдауне

    def open_first_result(self, query: str | None = None) -> None:
        self.first_result.evaluate("el => el.removeAttribute('target')")  # убирает target="_blank" чтобы открыть в том же окне
        self.first_result.click() # кликает на первую ссылку на страничке Поиск
        if query:
            expect(self.page).to_have_title(re.compile(query, re.IGNORECASE))  # ← проверяет что заголовок страницы содержит тикер