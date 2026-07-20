from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Выбор браузера для работы с сайтом
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.metatrader.com/en/symbols/nasdaq/nvda")
    page.screenshot(path="screenshot/HomePageNvda.png")
    page.close()

