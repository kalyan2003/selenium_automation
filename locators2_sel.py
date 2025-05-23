from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.automationexercise.com/")
driver.maximize_window()

dropdowns = driver.find_elements(By.CLASS_NAME,'panel-title')
print(len(dropdowns))
