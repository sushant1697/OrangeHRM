from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import sys
# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from locators.locators import Locators

class HomePage():

    def __init__(self,driver): # type: ignore
        self.driver = driver

        #These are the locatord for the elements
        self.user_link_class        = Locators.user_link_class
        self.logout_button_xpath    = Locators.logout_button_xpath
    
    #These are the different function for different actions
    def click_user(self):
        self.driver.find_element(By.CLASS_NAME,self.user_link_class).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_button_xpath).click()