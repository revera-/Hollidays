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
        view_page = View(self.browser)
        view_page._select_view('test01')
        view_page._check_view('test01')


    def test_create_new_view(self):
        """
        Тест создает и затем удаляет новое представление.
        1. залогинеться в ситемему
        2. открыть список представлений
        3. выбрать последний пункт из списка с именнем "Создать"
        4. Ввести имя нового представления "New_view"
        5. Выбрать списка доступных полей поле "Номер накладной BDF"
        6. Дважды кликнуть по полю чтоб оно перешло в список выбранны полей
        7. Нажать кнопку "Сохранить"

        :return:
        """

        self.login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        view_page._create_view("New_view")




