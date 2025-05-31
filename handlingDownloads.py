from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://vlc-media-player.en.softonic.com/download")
driver.implicitly_wait(10)
driver.maximize_window()

# Explicit wait for the span element to be clickable
wait = WebDriverWait(driver, 10)
span_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='kFckkm']//span[1]")))
span_element.click()

time.sleep(2)
