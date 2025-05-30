from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

dropdown_cnt = driver.find_elements(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select")

dropcountry = Select(dropdown_cnt[0])

dropcountry.select_by_visible_text("India")
dropcountry.select_by_index(12)
dropcountry.select_by_value("AFG")

for option in dropcountry.options:
    if option.text=="India":
        option.click()
        break

time.sleep(10)