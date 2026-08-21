import re
from playwright.sync_api import Locator, expect
from pages.base_page import BasePage


class NvdaBasePage(BasePage):
    BASE_URL = "https://www.metatrader.com/en/symbols/nasdaq/nvda"
    URL = BASE_URL

    # Locators

    @property
    def symbol_heading(self) -> Locator:
        return self.page.get_by_role("heading", name=re.compile("NVIDIA", re.IGNORECASE)).first

    # Actions

    def _assert_url(self) -> str | None:
        try:
            expect(self.page).to_have_url(re.compile(r"/nasdaq/nvda"))
            return None
        except AssertionError as e:
            lines = (l for l in str(e).splitlines() if l.strip())
            return "\n".join(
                l for l in lines
                if not l.startswith(("Call log", "Aria snapshot", "-", " "))
            )