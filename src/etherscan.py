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
    def __init__(self, username, email_address, password, email_confirmation):
        self.username = username
        self.email_address = email_address
        self.email_confirmation = email_confirmation
        self.password = password
        self.driver = initialize_driver()

    def insert_username(self, driver):
        username = driver.find_element(by=By.NAME, value="ctl00$ContentPlaceHolder1$txtUserName")
        time.sleep(2)
        username.send_keys(self.username)

    def insert_email_address(self, driver):
        driver = initialize_driver()
        email_address = driver.find_element(by=By.NAME, value="tl00$ContentPlaceHolder1$txtEmail")
        time.sleep(2)
        email_address.send_keys(self.email_address)

    def insert_email_confirmation(self, driver):
        driver = initialize_driver()
        email_confirmation = driver.find_element(by=By.NAME, value="tl00$ContentPlaceHolder1$txtEmail")
        time.sleep(2)
        email_confirmation.send_keys(self.email_confirmation)


