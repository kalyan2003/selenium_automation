from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

regLink = Keys.CONTROL+Keys.ENTER
driver.find_element(By.LINK_TEXT,"Register").send_keys(regLink)

time.sleep(3)
