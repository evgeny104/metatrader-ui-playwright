def test_search_nvda(page, home, results):
    """
    Клик по первой ссылки в -> dropdown -> page NVDA
    """
    query = "NVDA"
    home.search(query)
    results.should_be_opened()

def test_search_homepage(page, home, results):
    """
    Строка поиск ввод "Enter" - переход на страницу результатов
    """
    query = "NVIDIA"
    home.search(query, True)
    results.should_be_opened(True)






