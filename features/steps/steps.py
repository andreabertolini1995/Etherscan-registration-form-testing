import time
from src.etherscan import User
from behave import given, when, then
from selenium.webdriver.common.by import By

# Initialization
@given('a user on the Etherscan registration form')
def step_impl(context):
    context.user = User(website="https://etherscan.io/register")
    assert context.user.driver.title == "Etherscan Registration Page" 

  
@when('the user enters {value} as {field}')
def step_impl(context, field, value):
    entry = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$txt{field}")
    entry.send_keys(value)
    time.sleep(2)


@when('the user enters')
def step_impl(context):
    for row in context.table:
        entry = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$txt{row['field']}")
        entry.send_keys(row['value'])
        time.sleep(2)


# Error messages
@then('the user sees a {error} message saying {error_message}')
def step_impl(context, error, error_message):
    msg = context.user.driver.find_element(by=By.ID, value=f"ContentPlaceHolder1_txt{error}")
    assert msg.text == error_message
    context.user.driver.quit()


@then('there is no {error} message')
def step_impl(context, error):
    msg = context.user.driver.find_element(by=By.ID, value=f"ContentPlaceHolder1_txt{error}")
    assert msg.text == ""
    context.user.driver.quit()


@then('the user sees an error message saying "{error_message}"')
def step_impl(context, error_message):
    terms_conditions_error = context.user.driver.find_element(by=By.ID, value=f"ctl00$ContentPlaceHolder1$MyCheckBox-error")
    assert terms_conditions_error.text == error_message
    context.user.driver.quit()


@then('the user sees an alert saying "{error_message}"')
def step_impl(context, error_message):
    alert = context.user.driver.find_element(by=By.CLASS_NAME, value="alert-danger")
    assert error_message in alert.text
    context.user.driver.quit()


# Buttons
@when('the user clicks on the "Create an Account" button')
def step_impl(context):
    create_account_button = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$btnRegister")
    context.user.driver.execute_script("arguments[0].click();", create_account_button)
    time.sleep(20)
    

@when('the user accepts the Terms and Conditions')
def step_impl(context):
    terms_conditions = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$MyCheckBox")
    context.user.driver.execute_script("arguments[0].click();", terms_conditions)
    time.sleep(2)


@when('the user wants to receive Etherscan Newsletter')
def step_impl(context):
    newsletter = context.user.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$SubscribeNewsletter")
    context.user.driver.execute_script("arguments[0].click();", newsletter)
    time.sleep(2)


@when('the user proves not to be a robot')
def step_impl(context):
    check_robot = context.user.driver.find_element(by=By.CLASS_NAME, value="g-recaptcha")
    context.user.driver.execute_script("arguments[0].click();", check_robot)
    time.sleep(2)


# Extra
@then("the user is redirected to check if the connection is secure")
def step_impl(context):
    assert context.user.driver.title == "Just a moment..." 
