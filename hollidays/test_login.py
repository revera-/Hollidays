from bok_choy.web_app_test import WebAppTest
from hollidays.pages import PersonalAccountPage, LoginPage


class TestLogin(WebAppTest):
    """
    Тест логина в систему
    """
    def setUp(self):
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
        """
        self.login_page.visit().login('lara@lara.ru', '123123')
        account_page = PersonalAccountPage(self.browser)
        result = account_page.search_results
        print(' Проверяем возможность логина в систему test result = '+ str(result))


    def test_select_view(self):
        """
        выбор представления
        проверка представления по имени
        :return:
        """
        self.login_page.visit().login('lara@lara.ru', '123123')
        view_page = View(self.browser)
        view_page._select_view('test01')
        result = view_page._check_view('test01')
        print(result)
