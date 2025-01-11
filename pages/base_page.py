from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def open(self):
        """Переход на указаную ссылку"""
        self.page.goto(self.url)
    
    def wait_for_element(self, locator: str):
        """Ожидание появления элемента на странице"""  
        self.page.wait_for_selector(locator)
        
    def click_element(self, locator: str):
        """Клик по элементу"""
        self.page.click(locator)

    def fill_input(self, locator: str, value: str):
        """Заполнение поля ввода"""
        self.page.fill(locator, value)

    def select_option(self, locator: str, value: str):
        """Выбор опции в выпадающем списке"""
        self.page.select_option(locator, value)