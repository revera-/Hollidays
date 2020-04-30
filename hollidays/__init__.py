from bok_choy.web_app_test import WebAppTest
from hollidays.pages.login import LoginPage


class BaseWebTest(WebAppTest):
    def login(self, login, password):
        login_page = LoginPage(self.browser)
        login_page.visit()
        login_page.visit()
        login_page.login('lara@lara.ru', '123123')
