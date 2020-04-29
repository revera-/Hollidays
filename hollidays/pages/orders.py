from bok_choy.page_object import PageObject


class OrdersPage(PageObject):
    """
    Личный кабинет пользователя
    """
    url = 'https://tms-lite-test1.artlogics.ru/grid/orders'

    def is_browser_on_page(self):
        self.wait_for(lambda: self.q(css='.table').visible, "Table with orders was not visible to user")
        return self.browser.current_url == self.url
