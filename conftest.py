import pytest
import allure
import os
import shutil
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


@pytest.fixture(scope="session", autouse=True)
def set_environment():
    """Для отображения окружения в отчете"""
    with open("allure-results/environment.properties", "w") as f:
        f.write("OS=Windows 10\n")
        f.write("Chromium=131.0.6778.33\n")
        f.write("Firefox=132.0\n")
        f.write("WebKit=18.2\n")
        f.write("Python=3.13.1\n")
        f.write("Playwright=1.49.1\n")
        f.write("pytest=8.3.4\n")
        f.write("Allure=2.32.0\n")
        
@pytest.fixture(scope="session", autouse=True)
def save_allure_history():
    """Для сохранения истории отчетов"""
    history_dir = "allure-history"
    results_dir = "allure-results"

    if os.path.exists(history_dir):
        shutil.copytree(os.path.join(history_dir, "history"), os.path.join(results_dir, "history"), dirs_exist_ok=True)