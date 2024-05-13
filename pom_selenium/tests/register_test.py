import unittest

import pytest

from pages.register_page import RegisterPage


class RegisterTests(unittest.TestCase):

    def setUp(self) -> None:
        self.register_page = RegisterPage()
        self.register_page.open()

    def tearDown(self) -> None:
        self.register_page.close()

    @pytest.mark.smoke
    def test_pass_confirm_field_validation_for_min_length(self):
        self.register_page.set_first_name("Python")
        self.register_page.set_last_name("Automation")
        self.register_page.select_birth_year("1995")
        self.register_page.select_birth_month("May")
        self.register_page.select_birth_day("5")
        self.register_page.set_email("pyta14@gmail.com")
        self.register_page.set_password("12345")
        self.register_page.set_password_confirm("12345")
        self.register_page.click_register_button()
        self.register_page.verify_password_min_length_error_displayed()

    @pytest.mark.regression
    def test_register_page_url(self):
        self.register_page.verify_page_url("https://demo.nopcommerce.com/register")