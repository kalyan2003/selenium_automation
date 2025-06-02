import time
import mysql.connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
wait = WebDriverWait(driver, 15)

# Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="pavan2003",
    database="covid"
)
curs = con.cursor()
curs.execute("SELECT * FROM selenium_auto")
rows = curs.fetchall()

# Loop through each row in DB
for row in rows:
    try:
        price = row[0]
        rateofinterest = row[1]
        per1 = row[2]
        per2 = row[3]
        fre = row[4]
        exp_mvalue = row[5]

        # Fill the form
        driver.find_element(By.ID, "principal").clear()
        driver.find_element(By.ID, "principal").send_keys(str(price))

        driver.find_element(By.ID, "interest").clear()
        driver.find_element(By.ID, "interest").send_keys(str(rateofinterest))

        driver.find_element(By.ID, "tenure").clear()
        driver.find_element(By.ID, "tenure").send_keys(str(per1))

        Select(driver.find_element(By.ID, "tenurePeriod")).select_by_visible_text(per2)
        Select(driver.find_element(By.ID, "frequency")).select_by_visible_text(fre)

        # Try to close overlay ad if present
        try:
            overlay_close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wzrk-close")))
            overlay_close.click()
        except:
            pass  # Overlay not present

        # Click calculate
        calc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")))
        calc_btn.click()

        # Get result
        act_val = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='resp_matval']/strong"))).text
        act_val_clean = float(act_val.replace(',', ''))

        # Compare expected vs actual
        if abs(float(exp_mvalue) - act_val_clean) < 0.1:
            print(f"Pass | Expected: {exp_mvalue}, Actual: {act_val_clean}")
        else:
            print(f"Fail | Expected: {exp_mvalue}, Actual: {act_val_clean}")

        time.sleep(1)

    except Exception as e:
        print(f"Error in row {row}: {e}")
        continue

# Cleanup
driver.quit()
con.close()
