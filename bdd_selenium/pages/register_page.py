from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):

    ERROR_FIRST_NAME = (By.ID, "FirstName-error")
    ERROR_LAST_NAME = (By.ID, "LastName-error")
    EMAIL_ERROR = (By.ID, "Email-error")
    PASSWORD_ERROR = (By.ID, "Password-error")
    PASSWORD_CONFIRM_ERROR = (By.ID, "ConfirmPassword-error")
    TEXT_YOUR_PASSWORD = (By.XPATH, "//strong[text()='Your Password']")

    BUTTON_REGISTER = (By.ID, "register-button")

    def open(self):
        self.driver.get("https://demo.nopcommerce.com/register")

    def click_register_button(self):
        self.click(self.BUTTON_REGISTER)

    def verify_first_name_error_displayed(self):
        assert self.find(self.ERROR_FIRST_NAME).is_displayed(), "First name error is not displayed"
        assert self.find(self.ERROR_FIRST_NAME).text == "First name is required."


    def verify_last_name_error_displayed(self):
        assert self.find(self.ERROR_LAST_NAME).is_displayed(), "Last name error is not displayed"
        assert self.find(self.ERROR_LAST_NAME).text == "Last name is required."

    def verify_email_mandatory_error_displayed(self):
        assert self.find(self.EMAIL_ERROR).is_displayed(), "Email error is not displayed"
        assert self.find(self.EMAIL_ERROR).text == "Email is required."

    def verify_password_mandatory_error_displayed(self):
        assert self.find(self.PASSWORD_ERROR).is_displayed(), "Password error is not displayed"
        assert self.find(self.PASSWORD_ERROR).text == "Password is required."

    def verify_password_confirm_mandatory_error_displayed(self):
        assert self.find(self.PASSWORD_CONFIRM_ERROR).is_displayed(), "Password confirm error is not displayed"
        assert self.find(self.PASSWORD_CONFIRM_ERROR).text == "Password is required."

    def verify_password_min_length_error_displayed(self):
        assert self.find(self.PASSWORD_ERROR).is_displayed()
        assert self.find(self.PASSWORD_ERROR).text == "Password must meet the following rules:\nmust have at least 6 characters"

    def click_your_password_label(self):
        self.click(self.TEXT_YOUR_PASSWORD)