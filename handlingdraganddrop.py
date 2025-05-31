from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)

oslo_ele = driver.find_element(By.XPATH,"//div[@id='box1']")
norwa_ele = driver.find_element(By.XPATH,"//div[@id='box101']")

act.drag_and_drop(oslo_ele,norwa_ele).perform()
time.sleep(3)



