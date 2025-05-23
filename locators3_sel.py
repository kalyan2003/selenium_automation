from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Pavan kalyan")
driver.find_elements(By.CSS_SELECTOR,"input.inputtext")[1].send_keys("kaljd")

time.sleep(10)