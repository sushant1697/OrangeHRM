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

- **OrangeHRM Test Manager.py**  
  A desktop GUI application to create or update the `Config.json` file used for test configuration.

---

## OrangeHRM Test Manager (GUI Application)

This project includes a desktop-based GUI application:  
**OrangeHRM Test Manager.py**

### Functionality:
- **Create or update the test configuration file (`Config.json`)** in the `Json_Files` directory.
- **Edit all test parameters** such as Test URL, Incognito Mode, Drivers Type, Testing Browser, Headless Mode, Show Report, and Cross Browser Testing.
- **Select or change the location** of the config file if needed.
- **User-friendly interface** to manage test settings without editing JSON manually.

### How to use:
1. Run the GUI:
   ```
   python "OrangeHRM Test Manager.py"
   ```
2. Fill in or update the required test configuration fields.
3. Click **Save Config** to create or update the `Config.json` file in the `Json_Files` folder.
4. The test scripts will use this configuration for execution.

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
   Use the **OrangeHRM Test Manager** GUI or manually edit `Json_Files/Config.json` to set your browser, test URL, and other settings.

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
- Use the **OrangeHRM Test Manager** GUI for easy configuration management.

---

Feel free to add more test cases or page actions as needed!
