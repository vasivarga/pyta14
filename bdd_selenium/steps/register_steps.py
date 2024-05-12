from behave import *

@given("I am on the Register page")
def step_impl(context):
    context.register_page.open()

@then("First name mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_first_name_error_displayed()

@then("Last name mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_last_name_error_displayed()

@then("Email mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_email_mandatory_error_displayed()

@then("Password mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_password_mandatory_error_displayed()

@then("Password confirm mandatory error is displayed")
def step_impl(context):
    context.register_page.verify_password_confirm_mandatory_error_displayed()

@then("Password min length error is displayed")
def step_impl(context):
    context.register_page.verify_password_min_length_error_displayed()

@when("I click outside the password field")
def step_impl(context):
    context.register_page.click_your_password_label()

@When('I set "{text}" as first name')
def step_impl(context, text):
    context.register_page.set_first_name(text)

@When('I set "{text}" as last name')
def step_impl(context, text):
    context.register_page.set_last_name(text)

@When('I set "{text}" as email')
def step_impl(context, text):
    context.register_page.set_email(text)

@When('I select "{day}" "{month}" "{year}" as my birth date')
def step_impl(context, day, month, year):
    context.register_page.select_birth_day(day)
    context.register_page.select_birth_month(month)
    context.register_page.select_birth_year(year)

@When('I set a random valid email')
def step_impl(context):
    context.register_page.set_unique_email()

@When('I set "{text}" as password')
def step_impl(context, text):
    context.register_page.set_password(text)

@When('I set "{text}" as password confirmation')
def step_impl(context, text):
    context.register_page.set_password_confirm(text)

@when("I click Register button")
def step_impl(context):
    context.register_page.click_register_button()

@then('Success message is displayed')
def step_impl(context):
    context.register_page.verify_success_message_displayed()

@then('The success message is "{text}"')
def step_impl(context, text):
    context.register_page.verify_success_message_contains_text(text)