from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()

@when('I enter "{text}" as username')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('I enter "{text}" as password')
def step_impl(context, text):
    context.login_page.set_password(text)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('An error message is displayed')
def step_impl(context):
    context.login_page.verify_error_message_is_displayed()

@then('I should see "{text}"')
def step_impl(context, text):
    context.login_page.verify_error_message_text(text)

@then('The URL of the page is "{url}"')
def step_impl(context, url):
    context.login_page.verify_page_url(url)