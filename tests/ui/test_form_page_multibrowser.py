import pytest
import allure
from pages.form_page import FormPage
from links.page_urls import FormPageURLs


@allure.suite("Мультибраузерное тестирование формы")
@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
class TestFormPageMultiBrowser:

    @allure.title("Позитивный тест: Отправка формы с валидными данными (по умолчанию Offer)")
    @allure.description("Заполняем все поля валидными данными, оставляем выпадающий список как есть, нажимаем сабмит")
    @allure.tag("positive", "multibrowser")
    def test_submit_valid_data_offer(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(random_data["email"], random_data["names"], random_data["message_text"])
        form_page.submit_form()

    @allure.title("Позитивный тест: Отправка формы с валидными данными (Sale)")
    @allure.description("Заполняем все поля валидными данными, выбираем Sale, нажимаем сабмит")
    @allure.tag("positive", "multibrowser")
    def test_submit_valid_data_sale(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(random_data["email"], random_data["names"], random_data["message_text"], option="Sale")
        form_page.submit_form()

    @allure.title("Позитивный тест: Отправка формы с валидными данными (Discount)")
    @allure.description("Заполняем все поля валидными данными, выбираем Discount, нажимаем сабмит")
    @allure.tag("positive", "multibrowser")
    def test_submit_valid_data_discount(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(random_data["email"], random_data["names"], random_data["message_text"], option="Discount")
        form_page.submit_form()

    @allure.title("Негативный тест: Попытка отправки формы с пустыми полями")
    @allure.description("Нажимаем сабмит без заполнения полей")
    @allure.tag("negative", "multibrowser")
    def test_submit_empty_form(self, page):
        form_page = FormPage(page)
        form_page.open()
        form_page.submit_form()

    @allure.title("Негативный тест: Ввод слишком длинных значений в поля формы")
    @allure.description("Вводим максимальное количество символов в поля, нажимаем сабмит")
    @allure.tag("negative", "multibrowser")
    def test_submit_large_input(self, page):
        form_page = FormPage(page)
        form_page.open()
        large_text = "A" * 1000
        form_page.fill_form(large_text, large_text, large_text)
        form_page.submit_form()

    @allure.title("Негативный тест: Многократное нажатие на кнопку отправки")
    @allure.description("Заполняем форму валидными данными и нажимаем кнопку сабмит несколько раз подряд")
    @allure.tag("negative", "multibrowser")
    def test_submit_multiple_clicks(self, page, random_data):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(random_data["email"], random_data["names"], random_data["message_text"])
        for _ in range(5):
            form_page.submit_form()
    
    @allure.title("Негативный тест: ввод явно невалидного email")
    @allure.description("Вводим в поле email невалидные значения, которые должны вызвать ошибку, и проверяем появление валидационного сообщения.")
    @allure.tag("negative", "expected_failure", "multibrowser")
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
    @allure.tag("bug", "investigate", "multibrowser")
    def test_invalid_email_accepted_by_bug(self, page, invalid_email_accepted_by_bug, random_data):
        form_page = FormPage(page)
        form_page.open()
        
        form_page.fill_form(email=invalid_email_accepted_by_bug, name=random_data["names"], message=random_data["message_text"])
        form_page.submit_form()

        page.wait_for_timeout(2000)

        validation_message = page.locator('input[type="email"]').evaluate("el => el.validationMessage")
        
        assert not validation_message, f"Неожиданное валидационное сообщение для '{invalid_email_accepted_by_bug}', хотя сайт должен был его принять из-за ошибки."
