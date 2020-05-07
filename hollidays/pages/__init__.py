from urllib.parse import urljoin
from bok_choy.page_object import PageObject


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
        # заменила пока не работаю с run.py
        url = urljoin(self.kwargs.get('base_url', 'https://tms-lite-test1.artlogics.ru/'), self.path)
        # url = urljoin(self.kwargs.get('base_url', os.environ['TESTS_BASE_URL']), self.path)
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
