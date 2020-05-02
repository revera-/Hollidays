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
        view_page = OrdersPage(self.browser)
        assert view_page.is_browser_on_page()
        view_page.dropdown.select('last')  # выбираем Create
        assert view_page.modal_is_visible()

    def test_create_new_view(self):
        """
        Тест создает и затем удаляет новое представление.
        1. залогинеться в ситемему
        2. Создать новое представление
        3. проверить что пользователь находится в новом представлении
        # ! Важно: пока не реализовано удаление созданного представления, удалять руками
        """

        self.login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        view_page._create_view("New_view")
        view_page._check_view("New_view")

    def test_detete_new_view(self):
        """

        :return:
        """
        self.login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        name_view = "New_view1"
        view_page._create_view(name_view)
        view_page._check_view(name_view)
        view_page._delete_view(name_view)


