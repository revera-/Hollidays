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
        view_page._get_current_view_name('test01')


    def test_create_new_view(self):
        """
        Тест создает и затем удаляет новое представление.
        1. залогинеться в ситемему
        2. Создать новое представление
        3. проверить что пользователь находится в новом представлении
        # ! Важно: пока не реализовано удаление созданного представления, удалять руками
        """

        new_view_name = "New_view"
        self.login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        view_page._create_view(new_view_name)
        assert view_page._get_current_view_name() == new_view_name

    def test_detete_new_view(self):
        """

        :return:
        """
        self.login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        new_view_name = "New_view1"
        view_page._create_view(new_view_name)
        assert view_page._get_current_view_name() == new_view_name
        #view_page._get_current_view_name(name_view)
        view_page._delete_view(new_view_name)
        #добавить проверку что в списке нет представления


