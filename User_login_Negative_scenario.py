# Negative scenario: Attempt to log in with invalid credentials.

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj = Service(r"C:\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@id='login2']").click()
driver.find_element(By.ID, "loginusername").send_keys("homex")
driver.find_element(By.ID, "loginpassword").send_keys("tom13423")  # wrong password
driver.find_element(By.XPATH, "//button[@onclick='logIn()']").click()  # wrong password

time.sleep(5)

driver.quit()