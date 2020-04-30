from bok_choy.web_app_test import WebAppTest
from hollidays.pages.login import LoginPage
from hollidays.pages.orders import OrdersPage
from hollidays.pages.views import View
from hollidays import BaseWebTest


class TestView(BaseWebTest):
    """
    Тесты представления пользователя в гриде Заказы
    """

    def test_select_view(self):
        """
        выбор представления
        проверка представления по имени
        1. залогинеться в систему
        2. открыть список представлений
        3. выбрать представление по имени
        3. проверить чтоу пользователя открылось выбранное представление
        """
        self.login('lara@lara.ru', '123123')
        print ('login is done')
        view_page = View(self.browser)
        print("view_page is done")
        view_page._select_view('test01')
        result = view_page._check_view('test01')
        print(result)


