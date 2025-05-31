from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()

countries = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(4)