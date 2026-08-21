import re
import allure
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

    @allure.step("Ищем Компанию: {query}")
    def search(self, query: str, submit_with_enter: bool = False) -> None:
        with allure.step(f"Вводим '{query}' в строку поиска"):
            self.search_input.fill(query)

        if submit_with_enter:
            with allure.step("Отправляем поиск клавишей Enter"):
                self.page.keyboard.press("Enter")
        else:
            with allure.step("Ждём результаты и выбираем из дропдауна"):
                expect(
                    self.page.locator("header form div.list a.item").filter(has_text=query.upper()).first
                ).to_be_visible(timeout=10000)
                self.first_dropdown_item.click()

    @allure.step("Открываем первый результат поиска: {query}")
    def open_first_result(self, query: str) -> None:
        with allure.step("Открываем результат в текущей вкладке"):
            self.first_result.evaluate("el => el.removeAttribute('target')")
            self.first_result.click()
        with allure.step(f"Проверяем заголовок содержит '{query}'"):
            expect(self.page).to_have_title(re.compile(query, re.IGNORECASE))