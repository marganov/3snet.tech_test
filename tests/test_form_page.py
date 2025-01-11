import pytest
from pages.form_page import FormPage
from conftest import random_data
import allure



@pytest.mark.parametrize("browser", ["chromium", "firefox", "webkit"], indirect=True)
@pytest.mark.positive
class TestFormPage:
    @allure.title("Проверка открытия страницы формы")
    @allure.description("Тест проверяет, что страница формы открывается корректно")
    def test_open_form_page(page):
        form_page = FormPage(page)
        form_page.open()
        

    @allure.title("Проверка заполнения формы")
    @allure.description("Тест проверяет заполнение формы случайными валидными данными")    
    def test_fill_form(page):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(random_data["email"], random_data["names"], random_data["message_text"])
        assert form_page.page.input_value(form_page.locators.EMAIL_INPUT) == random_data["email"]
        assert form_page.page.input_value(form_page.locators.NAMES_INPUT) == random_data["names"]
        assert form_page.page.input_value(form_page.locators.MESSAGE_TEXT_INPUT) == random_data["message_text"]


    @allure.title("Проверка выбора опции Offer")
    @allure.description("Тест проверяет выбор опции Offer в форме")
    def test_select_offer(page):
        form_page = FormPage(page)
        form_page.open()
        form_page.select_offer()
        assert form_page.page.eval_on_selector(form_page.locators.SELECT_OPTION_OFFER, "el => el.value") == "Offer"


    @allure.title("Проверка выбора опции Sale")
    @allure.description("Тест проверяет выбор опции Sale в форме")
    def test_select_sale(page):
        form_page = FormPage(page)
        form_page.open()
        form_page.select_sale()
        assert form_page.page.eval_on_selector(form_page.locators.SELECT_OPTION_OFFER, "el => el.value") == "Sale"


    @allure.title("Проверка выбора опции Discount")
    @allure.description("Тест проверяет выбор опции Discount в форме")
    def test_select_discount(page):
        form_page = FormPage(page)
        form_page.open()
        form_page.select_discount()
        assert form_page.page.eval_on_selector(form_page.locators.SELECT_OPTION_OFFER, "el => el.value") == "Discount"


    @allure.title("Проверка отправки формы")
    @allure.description("Тест проверяет отправку формы с случайными данными")
    def test_submit_form(page):
        form_page = FormPage(page)
        form_page.open()
        form_page.fill_form(random_data["email"], random_data["names"], random_data["message_text"])
        form_page.submit_form()

