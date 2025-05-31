from selenium import webdriver

from selenium.webdriver.common.by import By


def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver



driver = headless_chrome()
driver.get("https://demo.nopcommerce.com")
print(driver.title)
print(driver.current_url)