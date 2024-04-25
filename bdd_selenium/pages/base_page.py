from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):

    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box-button")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def enter_search_term(self, text):
        self.type(self.SEARCH_INPUT, text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def verify_page_url(self, expected_url):
        assert self.driver.current_url == expected_url, "Error, unexpected page url"

    def verify_page_url_contains_text(self, text):
        assert text in self.driver.current_url, "Error, text not present in url"