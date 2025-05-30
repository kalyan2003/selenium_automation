from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")

alllinks = driver.find_elements(By.XPATH,"//a")

count = 0
for link in alllinks:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url," is broken link")
        count = count+1
    else:
        print(url," is valid link")

print("Invalid links are:",count)


