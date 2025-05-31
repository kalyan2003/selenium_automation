from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://ui.vision/demo/webtest/frames/")

frame1 = driver.find_element(By.XPATH,"//frame[@src='frame_1.html']")
driver.switch_to.frame(frame1)
form1 = driver.find_element(By.XPATH,"//input[@name='mytext1']")
form1.send_keys("pavan")
driver.switch_to.default_content()
frame2 = driver.find_element(By.XPATH,"//frame[@src='frame_2.html']")
driver.switch_to.frame(frame2)
form2 = driver.find_element(By.XPATH,"//input[@name='mytext2']")
form2.send_keys("Kalyan")
time.sleep(3)
