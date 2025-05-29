import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(5)

driver.close()