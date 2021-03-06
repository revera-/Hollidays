from bok_choy.web_app_test import WebAppTest

from hollidays.pages.elements import CREATE
from hollidays.pages.pages import LoginPage
from hollidays.pages.pages import OrdersPage
from hollidays.pages.views import View
from hollidays import BaseWebTest
import datetime



class TestView(BaseWebTest):
    """
    Тесты представления пользователя в гриде Заказы
    """
    def setUp(self):
        super(TestView, self).setUp()
        self.login('lara@lara.ru', '123123')

    def test_select_view(self):
        """
        выбор представления
        проверка представления по имени
        1. залогинеться в систему
        2. открыть список представлений
        3. выбрать представление по имени
        3. проверить что у пользователя открылось выбранное представление
        """
        # self.login('lara@lara.ru', '123123')
        view_page = OrdersPage(self.browser)
        assert view_page.is_browser_on_page()
        view_page.dropdown.select(CREATE)  # выбираем Create
        assert view_page.modal_is_visible()

    # def test_create_view(self):
    #     """
    #     Я как пользователь могу выбрать созждание нового представления из выпадающего списка и увидеть модальное окно
    #     с полями для создания представления.
    #     2. открыть список представлений
    #     3. выбрать представление по имени
    #     3. проверить что у пользователя открылось модальное окно для создания представления
    #     """
    #     view_page = OrdersPage(self.browser)
    #     assert view_page.is_browser_on_page()
    #     view_page.dropdown.select(CREATE)  # выбираем Create
    #     assert view_page.modal_is_visible()
    #     assert view_page.modal.input_visible()

    # def test_create_new_view(self):
    #     """
    #     Тест создает новое представление.
    #     1. залогинеться в ситемему
    #     2. Создать новое представление
    #     3. проверить что пользователь находится в новом представлении
    #     # ! Важно: пока не реализовано удаление созданного представления, удалять руками
    #     """
    #     new_view_name = "New_view " + (datetime.datetime.now()).strftime("%m-%d-%H:%M:%S")
    #     # self.login('lara@lara.ru', '123123')
    #     view_page = View(self.browser)
    #     view_page._create_view(new_view_name)
    #     assert view_page._get_current_view_name() == new_view_name

    def test_create_new_view(self):
        """
        Делаю новый тест на основе новой архитектуры классов
        Тест создает новое представление с уникальным именем.
        1. залогинеться в ситемему.
        2. Нажать на название текущего представления (левая часть хедора страницы)
          - откроется выпадающий список с набором доступных представлений
        3. выбрать самый последний пункт "+ Создать"
          - откроется модальное окно для создания нового представления
        4. Ввести уникальное название для нового представления
        5. Из списка доступных полей найти и выбрать поле "Номер накладно BDF".
        6. Дважды кликнуть по даному полю - поле переместиться в правую часть
        7. Нажать кнопку Сохранить
        8. Проверить что пользователь находится в новом представлении
        # ! Важно: пока не реализовано удаление созданного представления, удалять руками
        """
        name = "New_view " + (datetime.datetime.now()).strftime("%m-%d-%H:%M:%S")
        view_page = OrdersPage(self.browser)
        assert view_page.is_browser_on_page()
        view_page.dropdown.select(CREATE)  # выбираем Create
        assert view_page.modal_is_visible()
        new_name = view_page.modal.input_view_name() #вводим новое имя
        print(new_name)
        view_page.modal.find_and_add_fild('Номер накладной BDF')
        view_page.modal.submit() #7
        #добавить проверку: открыто новое представление №8


    def test_detete_new_view(self):
        """
        Тест последовательно создает, проверяет наличие и текущее положение,
        а затем удаляет новое представление с имененм new_view_name
        :return:
        """
        # self.login('lara@lara.ru', '123123')
        view_page: View = View(self.browser)
        new_view_name = "New_view " + (datetime.datetime.now()).strftime("%m-%d-%H:%M:%S")
        view_page._create_view(new_view_name)
        #проверка: созданное представлени сейчас активно
        assert view_page._get_current_view_name() == new_view_name
        view_page._delete_view(new_view_name)
        # проверка: в списке нет представления созданного ранее
        assert not(view_page._find_view_name_in_order(new_view_name))


