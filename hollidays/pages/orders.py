from hollidays.pages import BasePage, BaseContainer
from hollidays.pages.elements import DropdownElement
from bok_choy.browser import save_screenshot


DEFAULT = 'first'
PLANNED_DATES = 2
CREATE = 'last'


class SelectView(BaseContainer):
    locator = '.grid-header-panel .dropdown'
    menu_selector = '.menu'
    drop_down = DropdownElement(locator=menu_selector)  # our element

    def select_view(self, item_num):
        self.click()
        self.drop_down = item_num
        save_screenshot(self.page.browser, 'create')


class OrdersPage(BasePage):
    """
    Личный кабинет пользователя
    """
    path = '/grid/orders'

    def __init__(self, *args, **kwargs):
        super(OrdersPage, self).__init__(*args, **kwargs)
        self.view_select = SelectView(self)

    def is_browser_on_page(self):
        self.wait_for(lambda: self.q(css='.table').visible, "Table with orders was not visible to user")
        self.view_select.select_view('last')
        return self.browser.current_url == self.url
