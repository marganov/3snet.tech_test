from playwright.sync_api import Page
from pages.base_page import BasePage
from links.page_urls import FormPageURLs
from locators.form_page_locators import FormPageLocators


class FormPage(BasePage):
    """Класс страницы формы."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.url = FormPageURLs.FORM_PAGE_URL

    def open(self):
        """Открытие страницы формы."""
        self.page.goto(self.url)

    def get_title_text(self) -> str:
        """Получение текста заголовка формы."""
        return self.page.text_content(FormPageLocators.TITLE)

    def fill_form(self, email: str, name: str, message: str, option: str = "Offer"):
        """Заполнение формы."""
        self.page.fill(FormPageLocators.EMAIL_INPUT, email)
        self.page.fill(FormPageLocators.NAME_INPUT, name)
        self.page.fill(FormPageLocators.MESSAGE_INPUT, message)
        self.page.select_option(FormPageLocators.TYPE_DROPDOWN, option)

    def submit_form(self):
        """Нажатие на кнопку отправки формы."""
        self.page.click(FormPageLocators.SUBMIT_BUTTON)
