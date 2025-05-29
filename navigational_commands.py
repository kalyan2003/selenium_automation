from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait((10))
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")

driver.back()

driver.forward()

driver.refresh()

driver.quit()