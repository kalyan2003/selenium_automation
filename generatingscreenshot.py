from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

driver.save_screenshot("C:\\Users\\pavan\\Documents\\selenium_learning_project\\homepage.png")

