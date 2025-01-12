import requests
import allure
import pytest
from links.page_urls import FormPageURLs

@allure.suite("API Тестирование формы")
class TestFormAPI:
    
    @allure.title("Проверка доступности страницы формы")
    @allure.description("Отправляем GET-запрос и проверяем, что сервер отвечает статусом 200.")
    @allure.tag("api", "smoke")
    def test_get_form_page(self):
        response = requests.get(FormPageURLs.FORM_PAGE_URL)
        assert response.status_code == 200, f"Ошибка! Ожидали 200, получили {response.status_code}"

    @allure.title("Успешная отправка формы с валидными данными")
    @allure.description("Отправляем POST-запрос с валидными данными и ожидаем статус 200.")
    @allure.tag("api", "positive", "smoke")
    def test_post_valid_form(self, random_data):
        response = requests.post(FormPageURLs.FORM_PAGE_URL, data=random_data)
        assert response.status_code == 200, f"Ошибка! Ожидали 200, получили {response.status_code}"
    
    @allure.title("Отправка формы с невалидным email (ожидаемая ошибка)")
    @allure.description("Отправляем POST-запрос с невалидным email, который должен вызвать валидацию.")
    @allure.tag("api", "negative", "validation")
    def test_post_invalid_email_rejected(self, invalid_email_rejected):
        data = {"email": invalid_email_rejected, "name": "Test User", "message": "Test message"}
        response = requests.post(FormPageURLs.FORM_PAGE_URL, data=data)
        
        if response.status_code == 200:
            pytest.xfail(reason="Баг: сервер принимает невалидный email, ожидаем отказ.")
            
        assert response.status_code != 200, f"Ошибка! Ожидали отказ, но получили {response.status_code}"
    
    @allure.title("Отправка формы с невалидным email (который принимается из-за бага)")
    @allure.description("Отправляем POST-запрос с невалидным email, который система ошибочно принимает.")
    @allure.tag("api", "negative", "bug")
    def test_post_invalid_email_accepted_by_bug(self, invalid_email_accepted_by_bug, random_data):
        data = {"email": invalid_email_accepted_by_bug, "name": random_data["names"], "message": random_data["message_text"]}
        response = requests.post(FormPageURLs.FORM_PAGE_URL, data=data)

        # Ожидаем, что сервер отклонит запрос (например, 400 Bad Request), но он возвращает 200
        expected_status = 400  # Предположительное корректное поведение
        actual_status = response.status_code
        
        if actual_status == 200:
            pytest.xfail(reason="Баг: сервер принимает невалидный email, а должен был отклонить.")

        with allure.step(f"Проверяем, что сервер должен отклонить невалидный email: {invalid_email_accepted_by_bug}"):
            assert actual_status != 200, (
                f"БАГ: Сервер принял невалидный email ({invalid_email_accepted_by_bug}), но должен был вернуть ошибку! "
                f"Ожидалось: {expected_status}, получено: {actual_status}"
            )

        # Логируем для Allure
        allure.attach(
            f"Отправленные данные: {data}\n"
            f"Код ответа: {actual_status}\n"
            f"Тело ответа: {response.text}",
            name="API Response",
            attachment_type=allure.attachment_type.TEXT
        )
