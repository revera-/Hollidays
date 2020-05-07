import time

from hollidays.pages.Base.containers import SelectView
from hollidays.pages.Base.elements import CREATE
from hollidays.pages.orders import OrdersPage
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

    def test_user_can_select_view(self):
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
        view_page.wait_for_page()
        view_page.dropdown.select(CREATE)  # выбираем Create
        assert view_page.modal_is_visible()

    def test_user_can_create_new_view(self):
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
        view_page = OrdersPage(self.browser)
        view_page.wait_for_page()
        view_page.dropdown.select(CREATE)  # выбираем Create
        assert view_page.modal_is_visible()
        new_name = view_page.modal.set_view_name()  # вводим новое имя
        view_page.modal.add_field('Номер накладной BDF')
        view_page.modal.submit() #7
        assert view_page.dropdown.get_current_item == new_name

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
