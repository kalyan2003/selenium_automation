from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.adobe.com/in/acrobat/online/pdf-to-word.html")
driver.maximize_window()

# Wait for the page to load
time.sleep(5)

file_input = driver.find_element(By.XPATH, "//*[@id='fileInput']")
file_input.send_keys(r"C:\Users\pavan\OneDrive\Documents\IEEE_FINAL_PAPER.pdf")

time.sleep(5)
