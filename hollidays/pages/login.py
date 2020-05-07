from hollidays.pages import BasePage
from hollidays.pages.Base.containers import LoginForm, BaseContainer
from hollidays.pages.Base.elements import DropdownElement


RUSSIAN = 1


class LanguageSelector(BaseContainer):
    locator = '.language-switcher .dropdown'

    def set_option(self, option_order):
        dropdown = self.page.browser.find_element_by_css_selector(
            f'{self.locator} .menu .item:nth-child({option_order})'
        )
        self.page.browser.execute_script("arguments[0].click();", dropdown)


class LoginPage(BasePage):
    path = '/login'

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        self.form = LoginForm(self)
        self.language = LanguageSelector(self)

    def is_browser_on_page(self):
        self.form.wait_for_visible()
        return True

    def login(self, login, password):
        """
        Заполняем поля логин и пароль, нажимаем кнопку Войти.
        """
        self.language.set_option(RUSSIAN)
        self.form.submit(login, password)

