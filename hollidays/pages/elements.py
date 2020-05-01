"""
Elements library.
"""
from bok_choy.promise import EmptyPromise
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select


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


class DropdownElement(BaseElement):
    """
    Select element descriptor.
    """
    def __set__(self, obj, value):
        """
        Sets the value.
        """
        view_selector_map = {
            'first': '.item:first-child',
            'last': '.item:last-child',
        }
        element = self.get_page(obj).q(css=self.locator)[0]
        parent_locator = obj.locator
        elem_selector = f'{parent_locator} {view_selector_map[value]}'
        found = element.find_element_by_css_selector(elem_selector)
        print(found)
        found.click()

    def __get__(self, obj, owner):
        """
        Gets values for all selected options.
        """
        element = self.get_page(obj).q(css=self.locator)[0]
        # select = Select(element)
        # return [i.get_attribute("value") for i in select.all_selected_options]
