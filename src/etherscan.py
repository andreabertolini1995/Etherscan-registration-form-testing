import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class User:
    def __init__(self, website=None):
        self.driver = self.initialize_driver(website)

    def initialize_driver(self, website):
    
        service = ChromeService(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(website)
        driver.implicitly_wait(0.5)
        return driver

    def insert_value_in_form(self, username=None, email=None, confirm_email=None, password=None, confirm_password=None):

        placeholder = "ctl00$ContentPlaceHolder1$txt"
        if username:
            usr = self.driver.find_element(by=By.NAME, value=f"{placeholder}UserName")
            usr.send_keys(username)
        elif email:
            email_addr = self.driver.find_element(by=By.NAME, value=f"{placeholder}Email")
            email_addr.send_keys(email)
        elif confirm_email:
            confirm_email_addr = self.driver.find_element(by=By.NAME, value=f"{placeholder}ConfirmEmail")
            time.sleep(1)
            confirm_email_addr.send_keys(confirm_email)
        elif password:
            pwd = self.driver.find_element(by=By.NAME, value=f"{placeholder}Password")
            pwd.send_keys(password)
        elif confirm_password:
            confirm_pwd = self.driver.find_element(by=By.NAME, value=f"{placeholder}tPassword2")
            time.sleep(1)
            confirm_pwd.send_keys(confirm_password)
