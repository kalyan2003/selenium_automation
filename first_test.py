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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 10)


wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")


wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

# Title check
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

driver.close()
