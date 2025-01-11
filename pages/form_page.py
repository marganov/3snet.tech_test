from playwright.sync_api import Page
from .base_page import BasePage
from ..links.page_urls import FORM_PAGE_URL
from ..locators.form_page_locators import FormPageLocators


class FormPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = FORM_PAGE_URL
        self.locators = FormPageLocators()

    def open(self):
        """Переход на страницу формы"""
        super().open(self.url)
        

    def fill_form(self, email: str, names: str, message_text: str):
        """Заполнение формы"""
        self.fill_input(self.locators.EMAIL_INPUT, email)
        self.fill_input(self.locators.NAMES_INPUT, names)
        self.fill_input(self.locators.MESSAGE_TEXT_INPUT, message_text)

    def select_offer(self):
        """Выбор опции Offer"""
        self.select_option(self.locators.SELECT_OPTION_OFFER, "Offer")

    def select_sale(self):
        """Выбор опции Sale"""
        self.click_element(self.locators.SELECT_OPTION_SALE)

    def select_discount(self):
        """Выбор опции Discount"""
        self.click_element(self.locators.SELECT_OPTION_DISCOUNT)

    def submit_form(self):
        """Отправка формы"""
        self.click_element(self.locators.SUBMIT_BUTTON)
