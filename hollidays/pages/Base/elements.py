"""
Elements library.
"""
import time

from bok_choy.promise import EmptyPromise
from numpy.lib.user_array import container
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select


DEFAULT = 'first'
PLANNED_DATES = 2
CREATE = 'last'

class BaseElement:
    """
    Base class for all elements.
    """
    locator = None

    def __init__(self, locator=None):
        super(BaseElement, self).__init__()
        self.locator = locator if locator is not None else self.locator

    def get_page(self, obj):
        """
        Returns page instance for the given object.
        """
        return getattr(obj, 'page', obj)


class DropdownElement(BaseElement):
    """
    Select element descriptor.
    """
    OPTION_SELECTOR = '.item'
    view_selector_map = {
        DEFAULT: f'{OPTION_SELECTOR}:first-child',
        CREATE: f'{OPTION_SELECTOR}:last-child',
    }

    def __set__(self, container, value):
        """
        Choose the option.
        """
        page = self.get_page(container)
        container.click()  # раскрыть dropdown
        option_locator = self.view_selector_map.get(value, f'{self.OPTION_SELECTOR}:nth-child({value})')
        full_locator = f'{self.locator} {option_locator}'
        page.wait_for_element_visibility(  # wait for item in dropdown visible
            full_locator, "Dropdown option was not visible"
        )
        option = page.q(css=full_locator)  # div with option selected
        option.click()


class InputElement(BaseElement):
    """
    Input Text element descriptor.
    """
    def __set__(self, obj, value):
        """
        Sets the text to the value supplied.
        """
        # ищем на странице свой локатор
        element = self.get_page(obj).q(css=self.locator)

        def execute():
            """
            Fills a new value and indicates whether it is changed.
            """
            if value == "":
                # пример эмуляции того, что юзер стирает значение в поле
                raw_element = element.results[0]
                current_value = raw_element.get_attribute("value")
                for __ in current_value:
                    # тут можно вставить задержку time.sleep(0.5)
                    raw_element.send_keys(Keys.BACKSPACE)
            else:
                element.fill(value)

            return element.attrs("value")[0] == value

        # ждем пока не выполнится функция
        # промис ожидает, что функция вернет какое-то значение
        EmptyPromise(execute, "InputElement value is updated.").fulfill()

    def __get__(self, obj, owner):
        """
        Gets the text of the specified object
        """
        return self.get_page(obj).q(css=self.locator).attrs("value")[0]
        # return self.get_page(obj).q(css=self.locator).first.attrs("value")[0]


class FieldElement(BaseElement):
    """
    Набор полей для создания нового представления.
    Располагается в правой части модального окна при создании нового представления
    """
    def __set__(self, obj, field_name):
        self.get_page(obj).q(css='.label').first.click()
        element = self.get_page(obj).q(css='.label')
        ActionChains(self.get_page(obj).browser).double_click(element).perform()
        # пока не победила 2й клик: AttributeError: move_to requires a WebElement