from hollidays.pages import BasePage
from hollidays.pages.Base.containers import SelectView, ViewModal


class OrdersPage(BasePage):
    """
    Личный кабинет пользователя
    """
    dropdown: SelectView
    path = '/grid/orders'

    def __init__(self, *args, **kwargs):
        super(OrdersPage, self).__init__(*args, **kwargs)
        self.dropdown = SelectView(self)
        self.modal = ViewModal(self)

    def is_browser_on_page(self):
        self.wait_for(lambda: self.q(css='.table').visible, "Table with orders was not visible to user")
        return self.browser.current_url == self.url

    def modal_is_visible(self):
        self.modal.wait_for_visible()
        return True

    #def get_current_view_name(self):

