import random
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):

    INPUT_FIRST_NAME = (By.ID, "FirstName")
    INPUT_LAST_NAME = (By.ID, "LastName")
    SELECT_BIRTH_DAY = (By.NAME, "DateOfBirthDay")
    SELECT_BIRTH_MONTH = (By.NAME, "DateOfBirthMonth")
    SELECT_BIRTH_YEAR = (By.NAME, "DateOfBirthYear")
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    INPUT_PASSWORD_CONFIRM = (By.ID, "ConfirmPassword")
    BUTTON_REGISTER = (By.ID, "register-button")
    MESSAGE_SUCCESS = (By.CLASS_NAME, "result")

    ERROR_FIRST_NAME = (By.ID, "FirstName-error")
    ERROR_LAST_NAME = (By.ID, "LastName-error")
    EMAIL_ERROR = (By.ID, "Email-error")
    PASSWORD_ERROR = (By.ID, "Password-error")
    PASSWORD_LENGHT_ERROR = (By.CSS_SELECTOR, "[data-valmsg-for='Password']")
    PASSWORD_CONFIRM_ERROR = (By.ID, "ConfirmPassword-error")
    TEXT_YOUR_PASSWORD = (By.XPATH, "//strong[text()='Your Password']")

    def open(self):
        self.start()
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
        assert self.find(self.PASSWORD_LENGHT_ERROR).is_displayed()
        assert "must have at least 6 characters and not greater than 64 characters" in self.find(self.PASSWORD_LENGHT_ERROR).text

    def click_your_password_label(self):
        self.click(self.TEXT_YOUR_PASSWORD)

    def set_first_name(self, first_name):
        self.type(self.INPUT_FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.type(self.INPUT_LAST_NAME, last_name)

    def select_birth_day(self, text):
        self.select_dropdown_text(self.SELECT_BIRTH_DAY, text)

    def select_birth_month(self, text):
        self.select_dropdown_text(self.SELECT_BIRTH_MONTH, text)

    def select_birth_year(self, text):
        self.select_dropdown_text(self.SELECT_BIRTH_YEAR, text)

    # metoda pentru generare de adresa de email random
    def set_unique_email(self):
        number = random.randint(0, 9999999999999999)
        email_address = f"pyta14_{number}@gmail.com"
        self.set_email(email_address)

    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def set_password_confirm(self, text):
        self.type(self.INPUT_PASSWORD_CONFIRM, text)

    def verify_success_message_displayed(self):
        assert self.find(self.MESSAGE_SUCCESS).is_displayed(), "Success message is not displayed!"

    def verify_success_message_contains_text(self, text):
        assert self.find(self.MESSAGE_SUCCESS).text == text, "Success message is not correct!"