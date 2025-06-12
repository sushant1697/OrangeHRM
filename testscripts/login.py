from selenium import webdriver
import os
import selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
chromeOptions = webdriver.ChromeOptions()
edgeOptions = webdriver.EdgeOptions()
firefoxOptions = webdriver.FirefoxOptions()
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep, time
import unittest
import sys
import json
import HtmlTestRunner

# Add the parent directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.loginPage import LoginPage
from pages.homePage import HomePage

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config_loc = os.getcwd()+"/Json_Files/Config.json"
        file = open(config_loc,)
        data = json.load(file)
        test_url=data["drivers_config"]["Test_URL"]
        cross_browser_testing=data["drivers_config"]["Cross_Browser_Testing"]
        Testing_Browser=data["drivers_config"]["Testing_Browser"]
        Headless_mode=data["drivers_config"]["Headless_mode"]
        file.close()
        if Testing_Browser == "Chrome":
            if Headless_mode:
                chromeOptions.add_argument("--headless")
        elif Testing_Browser == "Edge":
            if Headless_mode:
                edgeOptions.add_argument("--headless")
        elif Testing_Browser == "Firefox":
            if Headless_mode:
                firefoxOptions.add_argument("--headless")
        if Testing_Browser == "Chrome":
            driver_loc = ChromeService(executable_path=os.getcwd() + "/drivers/chromedriver/chromedriver.exe")
            cls.driver = webdriver.Chrome(service=driver_loc,options=chromeOptions) 
        if Testing_Browser == "Edge":
            driver_loc = EdgeService(executable_path=os.getcwd() + "/drivers/edgedriver/msedgedriver.exe")
            cls.driver = webdriver.Edge(service=driver_loc,options=edgeOptions) 
        elif Testing_Browser == "Firefox":
            firefoxOptions.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"  # <-- Set your actual Firefox path here
            driver_loc = FirefoxService(executable_path=os.getcwd() + "/drivers/geckodriver/geckodriver.exe")
            print("Firefox Driver Location: ", driver_loc)
            cls.driver = webdriver.Firefox(service=driver_loc, options=firefoxOptions)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(test_url)

    def test_01_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        print("Login Pass")

    def test_02_logout_valid(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_user()
        homepage.click_logout()
        sleep(2)
        print("Logout Pass")

    def test_03_login_invalid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username("Admin_sky")
        login.enter_password("admin123")
        login.click_login()
        message = login.invalid_username_alert_xpath
        if message == "Invalid credentials":
            pass
            print("Invalid Login Check Pass")
        else:
            self.assertEqual(message, "Invalid credentials")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    current_directory = os.getcwd()
    config_loc = os.path.join(current_directory, "Json_Files", "Config.json")
    file = open(config_loc,)
    data = json.load(file)
    Show_Report = data["drivers_config"]["Show_Report"]
    cross_browser_testing = data["drivers_config"]["Cross_Browser_Testing"]
    Testing_Browser = data["drivers_config"]["Testing_Browser"]

    def run_tests():
        suite = unittest.TestLoader().loadTestsFromTestCase(Login)
        if Show_Report:
            runner = HtmlTestRunner.HTMLTestRunner(
                output='Testing_report',
                title="Login Page Test",
                report_name="Login",
                open_in_browser=True
            )
        else:
            runner = unittest.TextTestRunner()
        runner.run(suite)

    if cross_browser_testing:
        browsers = ["Chrome", "Edge", "Firefox"]
        for browser in browsers:
            data["drivers_config"]["Testing_Browser"] = browser
            with open(config_loc, "w") as f:
                json.dump(data, f, indent=4)
            print(f"\nRunning tests on {browser}...\n")
            run_tests()
    else:
        run_tests()