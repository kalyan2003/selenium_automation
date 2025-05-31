from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")

nrows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print("No of rows:",nrows);
ncols  = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print("No of cols:",ncols)

data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[2]/td[3]").text
print(data)

for r in range(2,nrows+1):
    for c in range(1,ncols+1):
        data = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[{c}]").text
        print(data)

    print(data)


for r in range(2,nrows+1):
    authorName = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[1]").text
        bookPrice = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{r}]/td[4]").text

        print(authorName,"  ",bookName,"  ",bookPrice)

