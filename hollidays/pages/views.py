from bok_choy.browser import save_screenshot
from bok_choy.page_object import PageObject
from selenium.webdriver.common.action_chains import ActionChains
import time


class View(PageObject):
    """
    Представление пользователя (заказы)
    """

    url = 'https://tms-lite-test1.artlogics.ru/grid/orders'

    def is_browser_on_page(self):
        self.wait_for(lambda: self.q(css='.table').visible, "Table with orders was not visible to user")
        return self.browser.current_url == self.url

    def _open_views_order(self):
        pass

    def _create_view(self, new_view_name):
        """
        Метод создает новое личное представление пользователя с мененем 'new_view_name'
        1. дожидаемся загрузки элемента select (проверяем возможность выбора представлени из списка)
        2. открываем список с доступными представлениями
        3. выбираем самый последний элемент из списка с названием "+ Создать"
        4. ожидаем что открывается модальное окно и появляются элементы для ввода данных
        5. вносим имя нового представления new_view_name
        6. Выбрать списка доступных полей поле "Номер накладной BDF"
        7. Дважды кликнуть по полю чтоб оно перешло в список выбранны полей
        8. Нажать кнопку "Сохранить"
        :param new_view_name: имя нового представления
        """
        #self.wait_for(lambda: self.q(xpath="//div[2]/div/div/div/div/div").visible,
        #              "Select  is not visible to user") #1
        self.wait_for(lambda: self.q(css=".fluid >.text").visible,
                      "Select  is not visible to user") #1

        #self.q(xpath="//div[2]/div/div/div/div/div").first.click()  #2
        self.q(css=".fluid >.text").first.click()


        self.q(xpath="//span[contains(.,'Создать')]").first.click()  #3
        self.wait_for(lambda: self.q(xpath="//form/div/div/input").visible,
                      "Input new_name_view is not visible to user")  # 4
        self.q(xpath ="//form/div/div/input").fill(new_view_name) #5

        self.wait_for(lambda: self.q(xpath="// div[34]/div").visible,
                      "Номер накладной BDF  is not visible to user")  #6

        #начало адского блока №7
        #тут сначала надо поле из списка проскролить и найти и выделить см.дейстиве ниже
        self.q(xpath="//div[34]/div").click()
        # а теперь можно двойным кликом его внести в список выбранных полей
        element = self.browser.find_element_by_xpath("//div[34]/div")
        ActionChains(self.browser).double_click(element).perform()
        # конец адского блока блока №7

        self.wait_for(lambda: self.q(xpath="//div[2]/button[2]").visible,
                      "Save button is not visible to user")  # ожидаем кнопку сохранить
        self.q(xpath="//div[2]/button[2]").click() #8
        self.wait_for(lambda: self.q(xpath="//div[2]/div/div/div/div/div").visible,
                      "Select  is not visible to user")  # ожидаем закрытие модалки
        # ! Важно: пока не реализовано удаление созданного представления, удалять руками

    def _delete_view(self, new_view_name):
        """
        1. проверяем возможность выбора представлени из списка
        2. выбираем представление по имени  new_view_name и оно становится текущим
        3. кликаем по кнопке "Настроить представление"
        4. ожидаем загрузки модалки с настройкой текущего представления
        5. находим кнопку "Удалить" и кликаем по ней
        6. подверждаем в новой модалке свои действия

        :param new_view_name:
        :return:
        """
        self.wait_for(lambda: self.q(css = ".fluid >.text").visible,
                      "Select  is not visible to user")  # 1
        self._select_view(new_view_name) #2
        self.q(xpath='//button/i').first.click() #3
        self.wait_for(lambda: self.q(xpath="//div[3]/div/button").visible,
                      "Delite button is not visible to user")  # 4
        self.q(xpath='//div[3]/div/button').first.click()  # 5
        self.wait_for(lambda: self.q(xpath="//div[5]/div/div[2]/button[2]").visible,
                      "Delite button is not visible to user")  # 6
        self.q(xpath='//div[5]/div/div[2]/button[2]').first.click()  # 6

    def _edit_view(self):
        pass

    def _select_view(self, name):
        """
        Метод производит поиск и выбор представления из списка доступных.
        :param name:
        :return: True
        """
        self.wait_for(lambda: self.q(css = ".fluid >.text").visible, "Select  is not visible to user")
        self.q(css = ".fluid >.text").first.click()
        view_path = "//span[contains(.,'" + name + "')]"
        self.q(xpath=view_path).first.click()

    def _rename_view(self):
        pass

    def _get_current_view_name(self):
        self.wait_for(lambda: self.q(css=".fluid >.text").visible, "Select  is not visible to user")
        view_name = self.q(css = ".fluid >.text").first.text
        view_name = str(view_name)[2:-2]
        return view_name

    def _find_view_name_in_order(self, view_name):
        """
        Метод производит поиск среди существующих представлений по заданному имени.
        !!! Найденное представление НЕ выбирает!!!
        1. Дожидаемся видимости жлемента дропдаун со списком представлений
        2. кликаем по нему для открытия списка
        3. дожидаемся отисовки списка
        4. ищем представление с заданным именем
        :return: true если представление нашли
        """
        self.wait_for(lambda: self.q(css=".fluid >.text").visible, "Select  is not visible to user")
        self.q(css=".fluid >.text").first.click()
        view_path = "//span[contains(.,'" + view_name + "')]"
        result =  self.q(xpath=view_path) == view_name
        return result
