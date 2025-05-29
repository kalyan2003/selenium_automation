from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demoqa.com/automation-practice-form")

email_input = driver.find_element(By.XPATH,"//input[@id='userEmail']")
email_input.send_keys("pavan@gmail.com")

print("email element text is:",email_input.text)
print("email element input text is:",email_input.get_attribute('value'))

driver.quit()