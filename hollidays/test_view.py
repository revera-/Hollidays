from bok_choy.web_app_test import WebAppTest
from hollidays.pages.login import LoginPage
from hollidays.pages.orders import OrdersPage, CREATE
from hollidays.pages.views import View
from hollidays import BaseWebTest
import datetime


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
        3. проверить что у пользователя открылось выбранное представление
        """
        self.login('lara@lara.ru', '123123')
        view_page = OrdersPage(self.browser)
        assert view_page.is_browser_on_page()
        view_page.dropdown.select(CREATE)  # выбираем Create
        assert view_page.modal_is_visible()

    def test_create_new_view(self):
        """
        Тест создает новое представление.
        1. залогинеться в ситемему
        2. Создать новое представление
        3. проверить что пользователь находится в новом представлении
        # ! Важно: пока не реализовано удаление созданного представления, удалять руками
        """
        new_view_name = "New_view " + (datetime.datetime.now()).strftime("%m-%d-%H:%M:%S")
        self.login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        view_page._create_view(new_view_name)
        assert view_page._get_current_view_name() == new_view_name

    def test_detete_new_view(self):
        """
        Тест последовательно создает, проверяет наличие и текущее положение,
        а затем удаляет новое представление с имененм new_view_name
        :return:
        """
        self.login('lara@lara.ru', '123123')
        view_page: View = View(self.browser)
        new_view_name = "New_view " + (datetime.datetime.now()).strftime("%m-%d-%H:%M:%S")
        view_page._create_view(new_view_name)
        #проверка: созданное представлени сейчас активно
        assert view_page._get_current_view_name() == new_view_name
        view_page._delete_view(new_view_name)
        # проверка: в списке нет представления созданного ранее
        assert not(view_page._find_view_name_in_order(new_view_name))


