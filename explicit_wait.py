from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

expliWait = WebDriverWait(driver, 10)
driver.get("https://demoqa.com/automation-practice-form")

firstname = expliWait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='firstName']")))
firstname.send_keys("Pavan")

submit_but = expliWait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit']")))
driver.execute_script("arguments[0].scrollIntoView();", submit_but)
submit_but.click()

driver.quit()
