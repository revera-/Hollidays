from bok_choy.browser import save_screenshot
from bok_choy.page_object import PageObject

class View(PageObject):
    """
    Представление пользователя (заказы)
    """

    url = 'https://tms-lite-test1.artlogics.ru/grid/orders'

    def is_browser_on_page(self):
        checks = [
            self.q(css='.container').visible,
            self.browser.current_url == self.url
        ]
        return all(checks)

    def _open_views_order(self):
        pass

    def _create_view(self):
        pass

    def _delite_view(self):
        pass

    def _edit_view(self):
        pass

    def _select_view(self, name):
        self.q(xpath="//div[2]/div/div/div/div/div").first.click()
        view_path = "//span[contains(.,'" + name + "')]"
        self.q(xpath=view_path).first.click()


    def _rename_view(self):
        pass


    def _check_view(self, name):
        view_name = self.q(xpath = '//div[2]/div/div/div/div/div/div').first.text
        view_name = str(view_name)[2:-2]
        return view_name