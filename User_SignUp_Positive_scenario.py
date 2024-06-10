# Positive scenario :- Signup with valid details
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

serv_obj = Service(r"C:\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@id='signin2']").click()
driver.find_element(By.ID, "sign-username").send_keys("homex")
driver.find_element(By.ID, "sign-password").send_keys("tom123")
driver.find_element(By.XPATH, "//button[@onclick='register()']").click()

time.sleep(5)

driver.quit()

