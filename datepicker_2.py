from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

date_picker = driver.find_element(By.XPATH,"//*[@id='dob']").click()

choose_month = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
choose_month.select_by_visible_text("Dec")
choose_year = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
choose_year.select_by_visible_text("2003")

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//tbody/tr/td/a")

for ele in dates:
    if ele.text=="9":
        ele.click()
        break

time.sleep(3)