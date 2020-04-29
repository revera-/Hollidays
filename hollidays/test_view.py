from bok_choy.web_app_test import WebAppTest
from hollidays.pages.login import LoginPage


class TestView(WebAppTest):
    """
    Тесты представления пользователя в гриде Заказы
    """

    def setUp(self):
        super(TestView, self).setUp()
        self.account_page = LoginPage(self.browser)

    def test_page_existence(self):
        """
        Проверяем что мы на странице логина
        """
        self.account_page.visit()

    def test_select_view(self, name = 'По умолчанию'):
        """
        Тест выбора представления из списка:
        1. залогинеться в систему
        2. открыть список представлений
        3. найти нужное представление
        4. выбрать и загрузить преставление
        5. проверить имя представления
        :param name: имя представления которое будем искать и открывать
        :return:
        """

