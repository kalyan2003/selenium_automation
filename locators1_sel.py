from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("iphone 16")
driver.find_element(By.LINK_TEXT,"Register").click()

# driver.close()