from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert_ele = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)
js_alert = driver.switch_to.alert
print(js_alert.text)
js_alert.send_keys("pavan")
js_alert.accept()
time.sleep(3)
