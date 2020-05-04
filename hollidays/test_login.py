from hollidays.pages.orders import OrdersPage
from hollidays.pages.views import View
from hollidays import BaseWebTest


class TestLogin(BaseWebTest):
    """
    Тест логина в систему
    """
    def test_user_lands_on_account_page(self):
        """
        Я, как пользователь из отдела продаж, могу увидеть список заказов
        на странице заказов после логина
        """
        self.login('lara@lara.ru', '123123')
        orders_page = OrdersPage(self.browser)
        orders_page.wait_for_page()
        order_rows = orders_page.q(xpath='//tr')
        assert len(order_rows) > 0

    def test_user_see_no_orders(self):
        """
        Я, как пользователь из отдела продаж, вижу отсутствие заказов если ...
        """
        # юзер не имеет заказов
        self.login('lara@lara.ru', '123123')
        orders_page = OrdersPage(self.browser)
        orders_page.wait_for_page()
        order_rows = orders_page.q(xpath='//tr')
        assert len(order_rows) == 0, "Unexpectedly got some orders"
