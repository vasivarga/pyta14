from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")
    ERROR_MEESAGE = (By.CSS_SELECTOR, "div.message-error li")

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/login")

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def verify_error_message_is_displayed(self):
        assert self.find(self.ERROR_MEESAGE).is_displayed(), "Error message was not displayed"

    def verify_error_message_text(self, expected):
        actual = self.find(self.ERROR_MEESAGE).text
        assert expected == actual, "Inavlid text!"


