import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demoqa.com/automation-practice-form")

first_name_ele = driver.find_element(By.XPATH,"//input[@id='firstName']")
first_name_ele.send_keys("Pavan")

time.sleep(5)
driver.quit()


