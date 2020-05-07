"""
Containers library.
"""
import time
from datetime import datetime
from bok_choy.browser import save_screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#from hollidays.pages import BaseElement
from hollidays.pages.Base.elements import InputElement, DropdownElement, FieldElement, BaseElement


class BaseContainer:
    """
    Base class for an element containing other elements.
    """
    locator = None

    def __init__(self, page, locator=None):
        self.page = page
        if locator:
            self.locator = locator

    def _get_full_locator(self, child_locator):
        return ' '.join([self.locator, child_locator])

    def find_nested_by_css(self, selector='', lookup_type='css'):
        """
        Returns nested elements.
        """
        query = {lookup_type: self._get_full_locator(selector)}
        return self.page.q(**query)

    def is_present(self):
        """
        Indicates whether element is present.
        """
        return self.page.q(css=self.locator).is_present()

    def is_visible(self):
        """
        Indicates whether element is visible.
        """
        return self.page.q(css=self.locator).visible

    def click(self):
        self.page.q(css=self.locator).click()

    def wait_for_visible(self, timeout=30):
        """
        Waiting until the element is visible. Raises BrokenPromise otherwise.
        """
        return self.page.wait_for_element_visibility(
            self.locator, "Element %s is visible" % self.locator, timeout=timeout
        )

    def wait_for_invisible(self, timeout=30):
        """
        Waiting until the element is invisible. Raises BrokenPromise otherwise.
        """
        return self.page.wait_for_element_invisibility(
            self.locator, "Element %s is invisible" % self.locator, timeout=timeout
        )

    def wait_for_absence(self, timeout=30):
        """
        Waiting until the element is invisible. Raises BrokenPromise otherwise.
        """
        return self.page.wait_for_element_absence(
            self.locator, "Element %s is invisible" % self.locator, timeout=timeout
        )

    def wait_for_nested_element(self, selector, description, timeout=30):
        if isinstance(selector, BaseElement):
            selector = selector.locator
        selector = self._get_full_locator(selector)
        self.page.wait_for_element_visibility(
            selector, description, timeout
        )

    def wait_for_element_clickable(self, selector, description, timeout=30):
        """
        Waits for element to be clickable.
        """
        self.page.wait_for(
            lambda: EC.element_to_be_clickable((By.ID, selector)),
            description,
            timeout=timeout
        )


class LoginForm(BaseContainer):
    locator = '.form'
    selectors = {
        'login': 'input[type="text"]',
        'password': 'input[type="password"]',
        'submit_btn': '.button'
    }

    login_input = InputElement(locator=selectors['login'])
    pass_input = InputElement(locator=selectors['password'])

    # def _enter_login(self, login):
    #     self.find_nested_by_css(self.selectors['login']).first.fill(login)

    # def _enter_password(self, password):
    #     self.find_nested_by_css(self.selectors['pass']).first.fill(password)

    def wait_for_visible(self, timeout=30):
        super(LoginForm, self).wait_for_visible()
        self.wait_for_nested_element(self.selectors['login'], "Login field was not visible")
        self.wait_for_nested_element(self.selectors['password'], "Password field was not visible")

    def submit(self, login, password):
        self.login_input = login
        self.pass_input = password
        self.find_nested_by_css(self.selectors['submit_btn']).first.click()


class ViewModal(BaseContainer):
    """
    Модалка создания/редактирования представления
    """
    locator = '#fieldModal.representation-modal'
    selectors = {
        'new_name': 'input[name="name"]',
        'new_field': '.label',
        'search_field': 'input[placeholder="Поиск поля"]'
        #'new_field': '//div[3]/div/div[2]/div/div/div/div/div/div'
    }
    name = InputElement(locator=selectors['new_name'])
    new_field = FieldElement(locator=selectors['new_field'])
    search_field = InputElement(locator=selectors['search_field'])
    #сюда добавить элементы модалки

    def set_view_name(self):
        # генерирует новое имя и заполняет поле "Наименование"
        new_name = "New_view " + (datetime.now()).strftime("%m-%d-%H:%M:%S")
        self.name = new_name
        return new_name

    def add_field(self, field_name):
        #находит и добавляет новое поле в блок "Выбранные поля"
        self.search_field = field_name
        self.new_field = field_name

    def submit(self):
        #Нажимаем кнопку Сохранить
        self.wait_for_element_clickable('button.ui.button.blue', 'Button is not clickable')
        self.find_nested_by_css('button.ui.button.blue').first.click()



class SelectView(BaseContainer):
    locator = '.grid-header-panel .field'
    options = DropdownElement(locator=locator)

    def select(self, item_num):
        self.options = item_num
        save_screenshot(self.page.browser, 'create')

    @property
    def get_current_item(self):
        self.wait_for_nested_element('div.text', 'View name is not ready')
        return str(self.find_nested_by_css('div.text').text)[2:-2]