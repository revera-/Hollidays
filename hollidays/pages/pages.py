"""
Pages library.
"""
from urllib.parse import urljoin
from bok_choy.page_object import PageObject
from hollidays.pages.containers import SelectView, LoginForm, ViewModal


class BasePage(PageObject):
    """
    Base page class.
    """
    path = None

    def __init__(self, browser, **kwargs):
        super(BasePage, self).__init__(browser)
        self.browser = browser
        self.kwargs = kwargs

    @property
    def url(self):
        """
        Construct url.
        """
        #заменила пока не работаю с run.py
        url = urljoin(self.kwargs.get('base_url', 'https://tms-lite-test1.artlogics.ru/'), self.path)
        #url = urljoin(self.kwargs.get('base_url', os.environ['TESTS_BASE_URL']), self.path)
        return url

    @property
    def title(self):
        """
        Returns page title.
        """
        return self.browser.title

    def text_is_visible(self, text):
        """
        Check if message "<text>" is visible
        """
        self.wait_for(
            lambda: self.q(xpath='//*[contains(text(), "{}")]'.format(text)).visible,
            "Check if text `{}` is visible".format(text),
            timeout=30
        )

    def refresh(self):
        """
        Refreshes the page.
        """
        self.browser.refresh()
        self.wait_for_page()


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
