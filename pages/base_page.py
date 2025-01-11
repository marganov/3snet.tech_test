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
        
    