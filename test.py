import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def initialize_driver():
    
    service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://etherscan.io/register")
    driver.implicitly_wait(0.5) # Understand exactly what this line is for
    return driver

# Rule: Registration is successful only if username is from 5 to 30 characters in length
def wrong_username_length():
    
    driver = initialize_driver()
    username = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtUserName")
    time.sleep(2)

    # email_address = driver.find_element(by=By.NAME, value=f"{placeholder}txtEmail")
    # confirm_email_address = driver.find_element(by=By.NAME, value=f"{placeholder}txtConfirmEmail")
    # password = driver.find_element(by=By.NAME, value=f"{placeholder}txtPassword")
    # confirm_password = driver.find_element(by=By.NAME, value=f"{placeholder}txtPassword2")
    # terms_conditions = driver.find_element(by=By.NAME, value=f"{placeholder}MyCheckBox")
    # newsletter = driver.find_element(by=By.NAME, value=f"{placeholder}SubscribeNewsletter")
    # check_robot = driver.find_element(by=By.CLASS_NAME, value="g-recaptcha")
    # create_account_button = driver.find_element(by=By.NAME, value=f"{placeholder} btnRegister")
    
    username.send_keys("Test")
    time.sleep(2)
    username_error = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtUserName-error")
    assert username_error.text == "Please enter at least 5 characters."

    time.sleep(2)
    driver.quit()


def correct_username():
    
    driver = initialize_driver()
    username = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtUserName")
    time.sleep(2)
    username.send_keys("Andrea")
    time.sleep(2)
    username_error = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtUserName-error")
    assert username_error.text == ""
    time.sleep(2)
    driver.quit()


def wrong_username_characters():
    
    driver = initialize_driver()
    # Find all the elements in the webpage
    username = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtUserName")
    time.sleep(2)
    username.send_keys("Andrea_")
    time.sleep(2)
    username_error = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtUserName-error")
    assert username_error.text == "Only alphanumeric characters allowed."
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':

    # Username checks
    wrong_username_length()
    wrong_username_characters()
    correct_username()

    # Email address checks






