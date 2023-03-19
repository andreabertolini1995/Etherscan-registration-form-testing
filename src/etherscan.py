from selenium import webdriver
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
