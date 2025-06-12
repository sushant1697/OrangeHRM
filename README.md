# OrangeHRM Selenium Test Automation

This project automates OrangeHRM web application testing using Selenium and Python.

---

## Page Object Model (POM)

This automated script **follows the Page Object Model (POM)** design pattern.

**What is POM?**  
Page Object Model is a design pattern in test automation that encourages the creation of separate classes for each page of the application.
- Each class contains locators for the web elements on that page and methods to interact with them.
- This makes the code more maintainable, reusable, and readable.

---

## Project Structure

- **locators/**  
  Contains locator definitions for web elements.  
  Each locator is grouped by page in the `locators` file.

- **pages/**  
  Contains Python classes for each page of the application.  
  Each class includes actions (methods) that can be performed on that page, using the locators from the `locators` file.

- **testscripts/**  
  Contains test scripts for different test cases.  
  Each script uses the page classes to perform actions and assertions.

---

## How to Run the Tests

1. **Install dependencies**  
   Make sure you have Python and pip installed.  
   Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. **Download WebDrivers**  
   Place the appropriate browser drivers (e.g., ChromeDriver, GeckoDriver for Firefox, EdgeDriver) in the `drivers` folder as specified in your config.

3. **Configure the Test**  
   Edit `Json_Files/Config.json` to set your browser, test URL, and other settings.

4. **Run a Test Script**  
   - Open the `testscripts/login.py` file.
   - Run the script using:
     ```
     python testscripts/login.py
     ```
   - This will execute the login-related test cases.

---

## Notes

- **Locators** for all elements are defined in the `locators` file.
- **Page actions** (like login, logout, etc.) are implemented in the `pages` folder, named according to the page (e.g., `loginPage.py` for the login page).
- **Test scripts** for different scenarios are in the `testscripts` folder.
- To run a specific test case, open the corresponding script in the `testscripts` folder and execute it.

---

Feel free to add more test cases or page actions as needed!
