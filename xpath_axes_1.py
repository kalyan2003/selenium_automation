from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
dri = webdriver.Chrome(service=service_obj)

dri.get("https://demo.nopcommerce.com/apparel")
input_val = dri.find_element(By.XPATH,"//form[@id='small-search-box-form']/child::input")
input_val.send_keys("t-shirts")

click_search = dri.find_element(By.XPATH,"//form[@id='small-search-box-form']/parent::div/child::form/child::button").click()

time.sleep(1000)



