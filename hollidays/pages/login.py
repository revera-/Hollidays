from hollidays.pages import BasePage, BaseContainer
from hollidays.pages.elements import InputElement


class LoginForm(BaseContainer):
    locator = '.form'
    selectors = {
        'login': 'input[type="text"]',
        'password': 'input[type="password"]',
        'submit_btn': '.button'
    }

    login_input = InputElement(locator=selectors['login'])
    pass_input = InputElement(locator=selectors['password'])

    # def _enter_login(self, login):
    #     self.find_nested_by_css(self.selectors['login']).first.fill(login)

    # def _enter_password(self, password):
    #     self.find_nested_by_css(self.selectors['pass']).first.fill(password)

    def wait_for_visible(self, timeout=30):
        super(LoginForm, self).wait_for_visible()
        self.wait_for_nested_element(self.selectors['login'], "Login field was not visible")
        self.wait_for_nested_element(self.selectors['password'], "Password field was not visible")

    def submit(self, login, password):
        self.login_input = login
        self.pass_input = password
        self.find_nested_by_css(self.selectors['submit_btn']).first.click()


class LoginPage(BasePage):
    path = '/login'

    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)
        self.form = LoginForm(self)

    def is_browser_on_page(self):
        self.form.wait_for_visible()
        return True

    def login(self, login, password):
        """
        Заполняем поля логин и пароль, нажимаем кнопку Войти.
        """
        self.form.submit(login, password)
