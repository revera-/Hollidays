import unittest
from bok_choy.web_app_test import WebAppTest
from Hollidays.pages import PersonalAссountPage, LoginPage



class TestLogin(WebAppTest):
    """
    Тест логина в систему
    """

    def setUp(self):
        """
        :return:
        """
        super(TestLogin, self).setUp()
        self.login_page = LoginPage(self.browser)

    def test_page_existence(self):
        """
        Проверяем что мы на странице логина
        """
        self.login_page.visit()

    def test_login(self):
        """
        Проверяем возможность логина в систему
        :return:
        """
        search_text = "TMS Lite"
        self.login_page.visit().login('lara@lara.ru', '123123')
        acount_page = PersonalAссountPage(self.browser)
        result = acount_page.search_results
        assert search_text in result[0]


if __name__ == '__main__':
    unittest.main()
