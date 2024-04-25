from browser import Browser
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_results_page import SearchResultsPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.register_page = RegisterPage()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()

def after_all(context):
    context.browser.close()
