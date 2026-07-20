from playwright.sync_api import sync_playwright


def get_total_revenue(url: str) -> dict[str, str]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # пока headless=False, видно что происходит
        page = browser.new_page()

        # 1. Меняем стратегию загрузки — не ждём networkidle
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        # 2. Ждём конкретный элемент — это надёжнее чем networkidle
        page.wait_for_selector(
            'label.row:has-text("Total revenue") span.cell[data-index]',
            timeout=30_000
        )

        # Заголовки годов
        header_text = page.locator('[class*="header"]').first.inner_text()
        years = [h for h in header_text.split() if h != "Value"]

        # Значения Total revenue
        cells = page.locator(
            'label.row:has-text("Total revenue") span.cell[data-index]'
        ).all()
        values = [
            c.inner_text().strip() for c in cells
            if c.inner_text().strip() != "Total revenue"
        ]

        browser.close()
        return dict(zip(years, values))


if __name__ == "__main__":
    url = "https://www.metatrader.com/en/symbols/nasdaq/nvda/statement"
    data = get_total_revenue(url)
    for year, val in data.items():
        print(f"{year}: {val}")