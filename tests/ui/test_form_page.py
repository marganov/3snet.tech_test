import pytest
import allure
from pages.form_page import FormPage


@allure.suite("Тестирование формы в дефолтном браузере")
@allure.feature("Форма отправки")
@pytest.mark.usefixtures("page")
class TestFormPage:
    
    @allure.title("Позитивный тест: отправка формы с валидными данными (по умолчанию Offer)")
    @allure.description("Заполняем все поля валидными данными и нажимаем кнопку отправки.")
    @allure.tag("positive")
    def test_submit_form_offer(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(
            email=random_data["email"], 
            name=random_data["names"], 
            message=random_data["message_text"]
        )
        form_page.submit_form()

    @allure.title("Позитивный тест: отправка формы с опцией Sale")
    @allure.description("Заполняем все поля валидными данными, выбираем Sale в выпадающем списке и нажимаем кнопку отправки.")
    @allure.tag("positive")
    def test_submit_form_sale(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(
            email=random_data["email"], 
            name=random_data["names"], 
            message=random_data["message_text"],
            option="Sale"
        )
        form_page.submit_form()

    @allure.title("Позитивный тест: отправка формы с опцией Discount")
    @allure.description("Заполняем все поля валидными данными, выбираем Discount в выпадающем списке и нажимаем кнопку отправки.")
    @allure.tag("positive")
    def test_submit_form_discount(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(
            email=random_data["email"], 
            name=random_data["names"], 
            message=random_data["message_text"],
            option="Discount"
        )
        form_page.submit_form()

    @allure.title("Негативный тест: отправка формы с пустыми полями")
    @allure.description("Нажимаем кнопку отправки формы без заполнения полей.")
    @allure.tag("negative")
    def test_submit_empty_form(self, page):
        form_page = FormPage(page)
        form_page.open()
        form_page.submit_form()

    @allure.title("Негативный тест: ввод большого количества символов в поля")
    @allure.description("Заполняем поля очень длинными строками и нажимаем кнопку отправки.")
    @allure.tag("negative")
    def test_submit_form_long_text(self, page):
        long_text = "A" * 10000
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(
            email=f"{long_text}@example.com", 
            name=long_text, 
            message=long_text
        )
        form_page.submit_form()

    @allure.title("Негативный тест: многократное нажатие на кнопку отправки")
    @allure.description("Заполняем поля валидными данными и многократно нажимаем кнопку отправки.")
    @allure.tag("negative")
    def test_submit_form_multiple_times(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(
            email=random_data["email"], 
            name=random_data["names"], 
            message=random_data["message_text"]
        )
        for _ in range(10):  # Нажимаем кнопку 10 раз
            form_page.submit_form()

    @allure.title("Негативный тест: ввод явно невалидного email")
    @allure.description("Вводим в поле email невалидные значения, которые должны вызвать ошибку, и проверяем появление валидационного сообщения.")
    @allure.tag("negative", "expected_failure")
    def test_invalid_email_submission(self, page, invalid_email_rejected, random_data):
        form_page = FormPage(page)
        form_page.open()
        
        form_page.fill_form(email=invalid_email_rejected, name=random_data["names"], message=random_data["message_text"])
        form_page.submit_form()

        page.wait_for_timeout(2000)

        validation_message = page.locator('input[type="email"]').evaluate("el => el.validationMessage")
        assert validation_message, f"Ожидалось валидационное сообщение для '{invalid_email_rejected}', но его нет."


    @allure.title("Баг-репорт: ввод невалидного email, который система ошибочно принимает")
    @allure.description("Вводим email, который должен считаться невалидным, но сайт ошибочно принимает его без валидации.")
    @allure.tag("bug", "investigate")
    def test_invalid_email_accepted_by_bug(self, page, invalid_email_accepted_by_bug, random_data):
        form_page = FormPage(page)
        form_page.open()
        
        form_page.fill_form(email=invalid_email_accepted_by_bug, name=random_data["names"], message=random_data["message_text"])
        form_page.submit_form()

        page.wait_for_timeout(2000)

        validation_message = page.locator('input[type="email"]').evaluate("el => el.validationMessage")
        
        assert not validation_message, f"Неожиданное валидационное сообщение для '{invalid_email_accepted_by_bug}', хотя сайт должен был его принять из-за ошибки."