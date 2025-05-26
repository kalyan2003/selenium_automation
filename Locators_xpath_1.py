from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/apparel")
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("iphone 16")

time.sleep(10)