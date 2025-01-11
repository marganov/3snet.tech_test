from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        """Базовый класс для всех страниц."""
        self.page = page

    def open(self, url: str):
        """Переход по указанному URL."""
        self.page.goto(url)
