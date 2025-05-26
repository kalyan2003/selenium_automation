# Selenium Automation Practice 

This repository contains my hands-on practice scripts using **Selenium WebDriver** with **Python**. These scripts demonstrate basic browser automation tasks such as form filling, interacting with web elements, performing searches, and validating conditions on various websites.

##  Technologies Used

- **Language**: Python  
- **Browser**: Google Chrome  
- **Library**: Selenium WebDriver  
- **Driver Path**: `C:\Drivers\chromedriver-win64\chromedriver.exe`

## Project Overview

This collection includes scripts demonstrating:

### 1. **Login Automation**
- **Website**: [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com)
- **Actions**: Automates login form, validates title after login.

### 2. **E-commerce Interaction**
- **Website**: [NopCommerce Demo](https://demo.nopcommerce.com)
- **Actions**: Performs product search (`iphone 16`), navigates to registration.

### 3. **UI Element Count**
- **Website**: [Automation Exercise](https://www.automationexercise.com)
- **Actions**: Counts number of dropdown panels using class name.

### 4. **Facebook Login Simulation**
- **Website**: [Facebook](https://www.facebook.com)
- **Actions**: Inputs dummy username and password using `CSS_SELECTOR`.

### 5. **Search Box Interaction**
- **Website**: [NopCommerce - Apparel Page](https://demo.nopcommerce.com/apparel)
- **Actions**: Sends search input and clicks using `XPath` with parent-child relationships.

## 🧠 What I Learned

- Handling **wait conditions** with `WebDriverWait` and `expected_conditions`
- Using various **locators**: `By.ID`, `By.NAME`, `By.XPATH`, `By.CSS_SELECTOR`, `By.LINK_TEXT`
- Navigating **DOM relationships** using XPath axes (`child::`, `parent::`)
- Managing browser sessions and options using `chrome_options`
- Working with **real-world websites** for practical automation experience




