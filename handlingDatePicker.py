from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# Switch to the frame that contains the datepicker
driver.switch_to.frame(0)

# Click on the input to open the date picker
driver.find_element(By.ID, "datepicker").click()

year = "2026"
month = "June"
date1 = "6"

# Loop until correct month and year are selected
while True:
    mon = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    ye = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if mon == month and ye == year:
        break

    # Click next button
    driver.find_element(By.XPATH, "//a[@title='Next']").click()
    time.sleep(0.1)

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//tbody/tr/td/a")

for ele in dates:
    if ele.text == date1:
        ele.click()
        time.sleep(1)
        break

