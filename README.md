OrangeHRM Selenium Test Automation
This project automates OrangeHRM web application testing using Selenium and Python.

Project Structure
locators/
Contains locator definitions for web elements.
Each locator is grouped by page in the locators file.

pages/
Contains Python classes for each page of the application.
Each class includes actions (methods) that can be performed on that page, using the locators from the locators file.

testscripts/
Contains test scripts for different test cases.
Each script uses the page classes to perform actions and assertions.

How to Run the Tests
Install dependencies
Make sure you have Python and pip installed.
Install required packages:

Download WebDrivers
Place the appropriate browser drivers (e.g., ChromeDriver, GeckoDriver for Firefox, EdgeDriver) in the drivers folder as specified in your config.

Configure the Test
Edit Config.json to set your browser, test URL, and other settings.

Run a Test Script

Open the login.py file.
Run the script using:
This will execute the login-related test cases.
Notes
Locators for all elements are defined in the locators file.
Page actions (like login, logout, etc.) are implemented in the pages folder, named according to the page (e.g., loginPage.py for the login page).
Test scripts for different scenarios are in the testscripts folder.
Feel free to add more test cases or page actions as needed! - This will execute the login-related test cases.

Notes
Locators for all elements are defined in the locators file.
Page actions (like login, logout, etc.) are implemented in the pages folder, named according to the page (e.g., loginPage.py for the login page).
Test scripts for different scenarios are in the testscripts folder.