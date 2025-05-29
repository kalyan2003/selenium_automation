from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print(element.text)

elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))

for ele in elements:
    print(ele.text)

driver.quit()