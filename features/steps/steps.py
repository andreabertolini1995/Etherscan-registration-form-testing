import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from src.etherscan import User


@given('a user with username "{username}", email address "{email_address}" and password "{password}"')
def step_impl(context, username, email_address, password):
    context.user = User(username=username, email_address=email_address, password=password)


@then('they see an username error message saying "{error_message}"')
def step_impl(context, error_message):
    username_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtUserName-error")
    assert username_error.text == error_message
    context.user.driver.quit()


@when('the user enters the username')
def step_impl(context):
    context.user.insert_username()


@then('there is no username error message')
def step_impl(context):
    username_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtUserName-error")
    assert username_error.text == ""
    context.user.driver.quit()


# Email address
@given('a user with email address "{email_address}"')
def step_impl(context, email_address):
    context.user = User(email_address=email_address)


@when('the user enters the email address')
def step_impl(context):
    context.user.insert_email_address()


@when('the user enters "{email_confirmation}" as the email confirmation')
def step_impl(context, email_confirmation):
    context.user.insert_email_confirmation(email_confirmation)


@then('they see a confirmation email error message saying "{error_message}"')
def step_impl(context, error_message):
    time.sleep(1)
    confirm_email_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtConfirmEmail-error")
    assert confirm_email_error.text == error_message
    context.user.driver.quit()


@then('there is no confirm email error message')
def step_impl(context):
    confirm_email_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtConfirmEmail-error")
    assert confirm_email_error.text == ""
    context.user.driver.quit()


# Password
@given('a user with email password "{password}"')
def step_impl(context, password):
     context.user = User(password=password)
    
    
@when('the user enters the password')
def step_impl(context):
    context.user.insert_password()


@when('the user enters "{another_password}" as the password confirmation')
def step_impl(context, another_password):
    context.user.confirm_password(another_password)


@then('they see a confirmation password error message saying "{error_message}"')
def step_impl(context, error_message):
    confirm_password_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtPassword2-error")
    assert confirm_password_error.text == error_message
    context.user.driver.quit()


@then('there is no confirm password error message')
def step_impl(context):
    confirm_password_error = context.user.driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtPassword2-error")
    assert confirm_password_error.text == ""
    context.user.driver.quit()


# Terms and conditions
@given('a user')
def step_impl(context):
    context.user = User()


@when('the user clicks on the "Create an Account" button')
def step_impl(context):
    create_account_button = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$btnRegister")
    context.user.driver.execute_script("arguments[0].click();", create_account_button)
    

@when('the user accepts the Terms and Conditions')
def step_impl(context):
    terms_conditions = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$MyCheckBox")
    context.user.driver.execute_script("arguments[0].click();", terms_conditions)


# @then('there is no T&C error message')
# def step_impl(context):
#     terms_conditions_error = context.user.driver.find_element(by=By.ID, value=f"ctl00$ContentPlaceHolder1$MyCheckBox-error")
#     assert terms_conditions_error.text == ""
#     context.user.driver.quit()


@when('the user does not accept the Terms and Conditions')
def step_impl(context):
    return # the user doesn't to anything here


@then('they see a T&C error message saying "{error_message}"')
def step_impl(context, error_message):
    terms_conditions_error = context.user.driver.find_element(by=By.ID, value=f"ctl00$ContentPlaceHolder1$MyCheckBox-error")
    assert terms_conditions_error.text == error_message
    context.user.driver.quit()

# Newsletter
@when('the user does not want to receive Etherscan Newsletter')
def step_impl(context):
    return # the user doesn't to anything here


# @when('the user wants to receive Etherscan Newsletter')
# def step_impl(context):
#     newsletter = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$SubscribeNewsletter")
#     context.user.driver.execute_script("arguments[0].click();", newsletter)

# Robot
@when('the user does not prove not be a robot')
def step_impl(context):
    return # the user doesn't to anything here


@then('they see an alert error message saying "{error_message}"')
def step_impl(context, error_message):
    alert = context.user.driver.find_element(by=By.CLASS, value="alert alert-danger")
    assert alert.text == error_message
    context.user.driver.quit()


when('the user proves not be a robot')
def step_impl(context):
    check_robot = context.user.driver.find_element(by=By.CLASS_NAME, value="g-recaptcha")
    context.user.driver.execute_script("arguments[0].click();", check_robot)


# Successful registration
@then('the user can successfully register to Etherscan')
def step_impl(context):
    print("Success!") # to be changed to what the user sees in the next page or so (probably with an assert)

