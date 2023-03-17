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

class User:
    def __init__(self, username=None, email_address=None, password=None):
        self.username = username
        self.email_address = email_address
        self.password = password
        self.driver = initialize_driver()

    def insert_username(self):
        username = self.driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtUserName")
        time.sleep(1)
        username.send_keys(self.username)

    def insert_email_address(self):
        email_address = self.driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtEmail")
        time.sleep(1)
        email_address.send_keys(self.email_address)

    def insert_email_confirmation(self, email_confirmation):
        confirm_email_address = self.driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtConfirmEmail")
        time.sleep(1)
        confirm_email_address.send_keys(email_confirmation)
    
    def insert_password(self):
        password = self.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$txtPassword")
        time.sleep(1)
        password.send_keys(self.password)

    def confirm_password(self, password_confirmation):
        confirm_password = self.driver.find_element(by=By.NAME, value=f"ctl00$ContentPlaceHolder1$txtPassword2")
        time.sleep(1)
        confirm_password.send_keys(password_confirmation)


