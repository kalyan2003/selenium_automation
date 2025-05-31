from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servserv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=servserv_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
ifrme_but = driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']")
ifrme_but.click()
time.sleep(2)

outerframe = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
innerframe = driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']")
driver.switch_to.frame(innerframe)
input_text = driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Pavan")
time.sleep(3)