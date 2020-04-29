from bok_choy.web_app_test import WebAppTest
from Hollidays.views import OrderView
from Hollidays.hollidays.pages import PersonalAccountPage, LoginPage

class TestView(WebAppTest):
    """
    Тесты представления пользователя в гриде Заказы
    """

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
        self.login_page.visit().login('lara@lara.ru', '123123')
        account_page = PersonalAccountPage(self.browser)
        account_page.

