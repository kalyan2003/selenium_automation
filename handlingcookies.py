from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com")

cookies = driver.get_cookies()
time.sleep(3)

driver.add_cookie({"name":"pavan","value":"123456789"})
print(len(cookies))

for c in cookies:
    print(c.get("name"),c.get("value"))

driver.delete_all_cookies()
