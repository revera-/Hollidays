"""
Containers library.
"""
import time
from datetime import datetime
from bok_choy.browser import save_screenshot
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from hollidays.pages import BaseElement
from hollidays.pages.elements import InputElement, DropdownElement


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
    locator = '#fieldModal.representation-modal'
    name = InputElement(locator='input[name="name"]')
    #search_fild = InputElement(locator='input[type="text"]').nth(2)
    #сюда добавить элементы модалки

    def input_view_name(self):
        new_name = "New_view " + (datetime.now()).strftime("%m-%d-%H:%M:%S")
        self.name = new_name
        return new_name

    def find_and_add_fild(self, fild_name):
        # не работает двойной клик
        search_fild = self.page.q(css='input[type="text"]').nth(2)
        search_fild.fill(fild_name)
        self.page.q(css='.label').first.click()
        element = self.page.q(css='.label').first
        time.sleep(5)
        #ActionChains(self.page.browser).double_click(element).perform()
        #search_fild.fill('') #очищаем поле поиска


    def submit(self):
        self.wait_for_element_clickable('button.ui.button.blue', 'Button is not clickable')
        self.find_nested_by_css('button.ui.button.blue').first.click()
        time.sleep(5)


class SelectView(BaseContainer):
    locator = '.grid-header-panel .field'
    options = DropdownElement(locator=locator)

    def select(self, item_num):
        self.options = item_num
        save_screenshot(self.page.browser, 'create')