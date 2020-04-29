import time
from bok_choy.browser import save_screenshot
from bok_choy.page_object import PageObject
from selenium.webdriver.common.keys import Keys



class LoginPage(PageObject):
    """
    Страница логина.
    """
    url = 'https://tms-lite-test1.artlogics.ru/login'

    def is_browser_on_page(self):
        self.wait_for_element_visibility('form', "Form not found on page")
        return True

    def _enter_login(self, login):
        self.q(xpath='//input[@name="login"]').first.fill(login)

    def _enter_password(self, password):
        self.q(xpath='//input[@name="password"]').first.fill(password)

    def _submit(self):
        self.q(xpath='//form/button').first.click()

    def login(self, login, password):
        """
        Заполняем поля логин и пароль, нажимаем кнопку Войти.
        """
        # поскольку поля ввода еще не отрисовались полностью (не добавлены в DOM)
        # нужно их подождать
        self.wait_for_element_visibility('input[type="text"]', "Error: Form is not loaded yet")
        self._enter_login(login)
        self._enter_password(password)
        self._submit()
        PersonalAccountPage(self.browser).wait_for_page()
        save_screenshot(self.browser, 'Login: after submit')


class PersonalAccountPage(PageObject):
    """
    Личный кабинет пользователя
    """
    url = 'https://tms-lite-test1.artlogics.ru/grid/orders'

    def is_browser_on_page(self):
        checks = [
            self.q(css='.container').visible,
            self.browser.current_url == self.url
        ]
        return all(checks)

    @property
    def search_results(self):
        title = self.browser.title
        return title == 'TMS Lite'
