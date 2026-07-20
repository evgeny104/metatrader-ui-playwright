import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Фикстура для браузера, редирект на страницу US"""
    return {
        **browser_context_args,
        "locale": "US",
    }