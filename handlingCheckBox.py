from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkBoxes = driver.find_elements(By.XPATH,"//input[@type = 'checkbox' and contains(@id,'checkBox')]")

for checkBox in checkBoxes:
    checkBox.click()

for checkBox in checkBoxes:
    if checkBox.is_selected():
        checkBox.click()

for checkBox in checkBoxes:
    id_name = checkBox.get_attribute('id')
    if id_name == "checkBoxOption1":
        checkBox.click()

time.sleep(10)

driver.quit()