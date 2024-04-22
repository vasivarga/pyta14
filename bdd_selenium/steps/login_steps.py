from behave import *

@given('I am on the login page')
def step_impl(context):
    context.login_page.open()

@when('I enter an invalid email')
def step_impl(context):
    context.login_page.set_email("pyta14@itf.ro")

@when('I enter a password')
def step_impl(context):
    context.login_page.set_password("123456767")

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('An error message is displayed')
def step_impl(context):
    context.login_page.verify_error_message_is_displayed()

@then('I should see "No customer account found"')
def step_impl(context):
    context.login_page.verify_error_message_text("No customer account found!")