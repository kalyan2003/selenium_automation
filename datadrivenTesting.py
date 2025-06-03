import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlUtils

# Setup
serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)

file = "C:\\Users\\pavan\\Downloads\\file_example_XLS_10.xlsx"
rows = xlUtils.getRowCount(file, "Sheet3")
nothanks_but = driver.find_element(By.XPATH,"//button[@id='wzrk-cancel']").click()

for r in range(2, rows + 1):
    price = xlUtils.readData(file, "Sheet3", r, 1)
    rateofinterest = xlUtils.readData(file, "Sheet3", r, 2)
    per1 = xlUtils.readData(file, "Sheet3", r, 3)
    per2 = xlUtils.readData(file, "Sheet3", r, 4)
    fre = xlUtils.readData(file, "Sheet3", r, 5)
    exp_mvalue = xlUtils.readData(file, "Sheet3", r, 6)

    driver.find_element(By.ID, "principal").clear()
    driver.find_element(By.ID, "principal").send_keys(price)

    driver.find_element(By.ID, "interest").clear()
    driver.find_element(By.ID, "interest").send_keys(rateofinterest)

    driver.find_element(By.ID, "tenure").clear()
    driver.find_element(By.ID, "tenure").send_keys(per1)

    Select(driver.find_element(By.ID, "tenurePeriod")).select_by_visible_text(per2)
    Select(driver.find_element(By.ID, "frequency")).select_by_visible_text(fre)

    # Handle overlay popup using WebDriverWait
    try:
        overlay_close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wzrk-close")))
        overlay_close.click()
    except:
        pass  # Overlay didn't appear

    # Wait for Calculate button and click it
    calc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")))
    calc_btn.click()

    # Wait for result to appear
    act_val = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='resp_matval']/strong"))).text

    if float(exp_mvalue) == float(act_val.replace(',', '')):
        print("Pass")
        xlUtils.writeData(file, "Sheet3", r, 8, "Pass")
    else:
        print("Fail")
        xlUtils.writeData(file, "Sheet3", r, 8, "Fail")

time.sleep(3)
driver.quit()
