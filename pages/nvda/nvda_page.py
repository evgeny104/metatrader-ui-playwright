import re
from pages.base_page import BasePage
from playwright.sync_api import Locator, expect


class NvdaBasePage(BasePage):
    BASE_URL = "https://www.metatrader.com/en/symbols/nasdaq/nvda"  # URL страницы NVDA, используется в дочерних классах
    URL = BASE_URL  # переопределяется в дочерних классах

    # Locators

    @property
    def symbol_heading(self) -> Locator:
        return self.page.get_by_text(re.compile("NVIDIA", re.IGNORECASE)).first  # достает заголовок с названием NVIDIA

    # Actions

    def should_be_opened(self) -> None:
        expect(self.page).to_have_url(self.URL)  # ← проверяет URL страницы
