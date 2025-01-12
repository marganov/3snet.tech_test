import pytest
from utils.data_generator import DataGenerator


@pytest.fixture(scope="function")
def random_data():
    """Фикстура для создания случайных валидных данных"""
    return DataGenerator.generate_random_data()

@pytest.fixture(scope="function")
def invalid_email_rejected():
    return DataGenerator.generate_invalid_email_rejected()

@pytest.fixture(scope="function")
def invalid_email_accepted_by_bug():
    return DataGenerator.generate_invalid_email_accepted_by_bug()

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
