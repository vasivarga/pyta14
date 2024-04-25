from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/")