import pytest
from playwright.sync_api import sync_playwright
import requests
from faker import Faker


def pytest_addoption(parser):
    """Опция --headless, которая позволяет запускать браузер в безголовом режиме"""
    parser.addoption("--headless", action="store_true", default=True, help="False для отображения браузеров во время теста")

@pytest.fixture(scope="session")
def headless(request):
    return request.config.getoption("--headless")


# Фикстура для запуска браузера, параметризованная для Chromium, Firefox и WebKit
@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser(request):
    # Получаем имя браузера из параметра
    browser_name = request.param
    # Инициализируем Playwright
    with sync_playwright() as p:
        # В зависимости от имени запускаем соответствующий браузер
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=headless) 
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=headless) 
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=headless) 
        
        yield browser
        browser.close()

# Фикстура для создания новой страницы в браузере и закрытия страницы после тестов
@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()

# Фикстура для создания HTTP-сессии
@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()
    
# Фикстура для генерации случайных данных при заполнении полей для почты, имени и набора текста
@pytest.fixture(scope="function")
def random_data():
    fake = Faker()
    data = {
        "email": fake.email(),
        "names": fake.name(),
        "message_text": fake.text()
    }
    return data