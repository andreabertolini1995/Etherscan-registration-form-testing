from behave import given, when, then
from src.etherscan import User

@given('a user with email address "{text}"')
def set_email_address(context, email_address):
    user = User(email_address = email_address)
    context.user = user

@when('the user enters the email address')
def enter_email_address(context):
    context.user.insert_email_address()

@when('the user enters "{text}" as the email confirmation')
def enter_email_address(context, email_confirmation):
    context.user.email_confirmation = email_confirmation
    context.user.insert_email_confirmation()

@when('the email address is different than the confirmation')
def is_confirmed_email_wrong(context):
    assert context.user.email_address != context.user.email_confirmation

@then('there is an error message')
def error_message_confirmation_email(context):
    confirm_email_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtConfirmEmail-error")
    assert confirm_email_error.text == "Email address does not match."


""" What to do next:
1. With Python's behave, probably the structure of the folder would look quite differently. Since I have it already set up like this now, it might be 
    worth it trying using JS with the Selenium functions and have the whole thing in JavaScript.
2. JavaScript looks complicated though, so I think I'll try to stick with Python and behave. """