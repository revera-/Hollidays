from hollidays.pages import BasePage, BaseContainer
from hollidays.pages.elements import BaseElement
from bok_choy.browser import save_screenshot


DEFAULT = 'first'
PLANNED_DATES = 2
CREATE = 'last'


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


class SelectView(BaseContainer):
    locator = '.grid-header-panel .field'
    options = DropdownElement(locator=locator)

    def select(self, item_num):
        self.options = item_num
        save_screenshot(self.page.browser, 'create')


class Modal(BaseContainer):
    locator = '#fieldModal.representation-modal'


# class OrderStatusFilter(BaseContainer):
#     locator = '.loc'
#
#     in
#
#     def
#
# class ClientsFilter(BaseContainer):
#     locator = '.loc'
#
#
# class Table(BaseContainer):
#     locator = '.table'
#
#     def __init__(self, *args, **kwargs):
#         super(Table, self).__init__(*args, **kwargs)
#         self.order_status = OrderStatusFilter(self.page)
#         self.client = ClientsFilter(self.page)
#         ...


class OrdersPage(BasePage):
    """
    Личный кабинет пользователя
    """
    path = '/grid/orders'

    def __init__(self, *args, **kwargs):
        super(OrdersPage, self).__init__(*args, **kwargs)
        self.dropdown = SelectView(self)
        self.modal = Modal(self)

    def is_browser_on_page(self):
        self.wait_for(lambda: self.q(css='.table').visible, "Table with orders was not visible to user")
        return self.browser.current_url == self.url

    def modal_is_visible(self):
        self.modal.wait_for_visible()
        return True
