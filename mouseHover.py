from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 10)

# Wait for username field and send keys
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("Admin")

# Wait for password field and send keys
password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Wait for login button and click
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()
admin_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")))

manage_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='User Management']")))
users_click = wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")))

mousHove = ActionChains(driver)
mousHove.move_to_element(admin_menu).move_to_element(manage_dropdown).move_to_element(users_click).click().perform()