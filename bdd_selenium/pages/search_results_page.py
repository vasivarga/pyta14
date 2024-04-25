from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    DIV_PRODUCT_TITLE = (By.CLASS_NAME, "product-title")

    def verify_search_results_are_displayed(self):
        results_list = self.find_all(self.DIV_PRODUCT_TITLE)
        assert len(results_list) > 0, "Error, no results found"
