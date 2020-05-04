import os
from urllib.parse import urljoin
from bok_choy.page_object import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from hollidays.pages.elements import InputElement, BaseElement


class BaseContainer:
    """
    Base class for an element containing other elements.
    """
    locator = None

    def __init__(self, page, locator=None):
        self.page = page
        if locator:
            self.locator = locator

    def _get_full_locator(self, child_locator):
        return ' '.join([self.locator, child_locator])

    def find_nested_by_css(self, selector='', lookup_type='css'):
        """
        Returns nested elements.
        """
        query = {lookup_type: self._get_full_locator(selector)}
        return self.page.q(**query)

    def is_present(self):
        """
        Indicates whether element is present.
        """
        return self.page.q(css=self.locator).is_present()

    def is_visible(self):
        """
        Indicates whether element is visible.
        """
        return self.page.q(css=self.locator).visible

    def click(self):
        self.page.q(css=self.locator).click()

    def wait_for_visible(self, timeout=30):
        """
        Waiting until the element is visible. Raises BrokenPromise otherwise.
        """
        return self.page.wait_for_element_visibility(
            self.locator, "Element %s is visible" % self.locator, timeout=timeout
        )

    def wait_for_invisible(self, timeout=30):
        """
        Waiting until the element is invisible. Raises BrokenPromise otherwise.
        """
        return self.page.wait_for_element_invisibility(
            self.locator, "Element %s is invisible" % self.locator, timeout=timeout
        )

    def wait_for_absence(self, timeout=30):
        """
        Waiting until the element is invisible. Raises BrokenPromise otherwise.
        """
        return self.page.wait_for_element_absence(
            self.locator, "Element %s is invisible" % self.locator, timeout=timeout
        )

    def wait_for_nested_element(self, selector, description, timeout=30):
        if isinstance(selector, BaseElement):
            selector = selector.locator
        selector = self._get_full_locator(selector)
        self.page.wait_for_element_visibility(
            selector, description, timeout
        )

    def wait_for_element_clickable(self, selector, description, timeout=30):
        """
        Waits for element to be clickable.
        """
        self.page.wait_for(
            lambda: EC.element_to_be_clickable((By.ID, selector)),
            description,
            timeout=timeout
        )


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
