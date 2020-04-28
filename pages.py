import re
from bok_choy.page_object import PageObject


class LoginPage(PageObject):
    """
    Станица логина
    """

    url = 'https://tms-lite-test1.artlogics.ru/login'

    def is_browser_on_page(self):
        print('is_browser_on_page')
        return 'TMS Lite' in self.browser.title

    def enter_login(self, login):
        print('enter_login')
        return self.q(css="input[name='login']").fill(login)


    def enter_password(self, password):
        print('enter_password')
        return self.q(css="input[name='password']").fill(password)


    def press_button_login(self):
        self.q(css='button[api=object Object]')
        PersonalAссountPage(self.browser).wait_for_page()
        print('press_button_login')


    def login(self, login, password):
        """
        Заполняем поля логин и пароль.
        Нажимет кнопку Войти.
        """
        self.enter_login(login)
        self.enter_password(password)
        self.press_button_login()
        print('login')



class PersonalAссountPage(PageObject):
    """
    Личный кабинет пользователя
    """
    url = None

    def is_browser_on_page(self):
        print('is_browser_on_page')
        return self.q(css='.header - support_contacts').is_present


    @property
    def search_results(self):
        print('search_results')
        title = self.browser.title
        return title == 'TMS Lite'
