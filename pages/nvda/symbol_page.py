import allure
from playwright.sync_api import expect
from pages.nvda.nvda_page import NvdaBasePage


class NvdaSymbolPage(NvdaBasePage):
    URL = NvdaBasePage.BASE_URL

    @allure.step("Проверяем страницу символа NVDA")
    def should_be_opened(self) -> None:
        with allure.step("URL содержит /nasdaq/nvda"):
            if msg := self._assert_url():
                raise AssertionError(msg)
        with allure.step("Заголовок NVIDIA виден на странице"):
            expect(self.symbol_heading).to_be_visible()