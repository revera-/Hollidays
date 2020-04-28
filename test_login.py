import unittest
from bok_choy.web_app_test import WebAppTest
from Hollidays.pages import PersonalAссountPage, LoginPage


class TestLogin(WebAppTest):
    """
    Тест логина в систему
    """

    def setUp(self):
        super(TestLogin, self).setUp()
        self.login_page = LoginPage(self.browser)
        print('setUp')


    def test_page_existence(self):
        """
        Проверяем что мы на странице логина
        """
        print('Проверяем что мы на странице логина test_page_existence')
        self.login_page.visit()


    def test_login(self):
        """
        Проверяем возможность логина в систему
        """
        self.login_page.visit().login('lara@lara.ru', '123123')
        acount_page = PersonalAссountPage(self.browser)
        result = acount_page.search_results
        print(' Проверяем возможность логина в систему test result = '+ str(result))


if __name__ == '__main__':
    unittest.main()
