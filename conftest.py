import pytest
from faker import Faker


@pytest.fixture(scope="function")
def random_data():
    """Фикстура для генерации случайных данных для тестов"""
    fake = Faker()
    return {
        "email": fake.email(),
        "names": fake.name(),
        "message_text": fake.text(),
    }


@pytest.fixture(scope="session")
def context(browser):
    """Создание контекста с игнорированием ошибок HTTPS"""
    context = browser.new_context(ignore_https_errors=True)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """Создание новой страницы в контексте"""
    page = context.new_page()
    yield page
    page.close()
