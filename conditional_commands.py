from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Register.html")

first_name_box = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
last_name_box = driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")

print("Display status",first_name_box.is_displayed())
print("Enabled status",last_name_box.is_enabled())

male_drop = driver.find_element(By.XPATH,"//input[@value='Male']")
female_drop = driver.find_element(By.XPATH,"//input[@value='FeMale']")

male_drop.click()

time.sleep(2)
print("selected status",male_drop.is_selected())
print("selected status",female_drop.is_selected())

driver.quit()
