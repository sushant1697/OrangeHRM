from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import sys
# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators.locators import Locators

class LoginPage():

    def __init__(self,driver): # type: ignore
        self.driver = driver

        #These are the locatord for the elements
        self.username_textbox_name  = Locators.username_textbox_name
        self.password_textbox_name  = Locators.password_textbox_name
        self.login_button_css       = Locators.login_button_css
        self.invalid_username_alert_xpath = Locators.invalid_username_alert_xpath
    
    #These are the different function for different actions
    def enter_username(self,username):
        self.driver.find_element(By.NAME,self.username_textbox_name).clear()
        self.driver.find_element(By.NAME,self.username_textbox_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME,self.password_textbox_name).clear()
        self.driver.find_element(By.NAME,self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR,self.login_button_css).click()

    def check_invalid_username_alert(self,message):
        msg =   self.driver.find_element(By.XPATH,self.invalid_username_alert_xpath).text
        return msg