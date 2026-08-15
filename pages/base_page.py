from playwright.sync_api import Page

class BasePage:

    def __init__(self, page: Page):
        self.page = page  # объект браузера от Playwright, доступен во всех наследниках

