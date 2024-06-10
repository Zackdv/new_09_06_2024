# Verify that products are displayed correctly on the homepage.

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service(r"C:\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@id='login2']").click()
driver.find_element(By.ID, "loginusername").send_keys("homex")
driver.find_element(By.ID, "loginpassword").send_keys("tom123")
driver.find_element(By.XPATH, "//button[@onclick='logIn()']").click()


element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='tbodyid']//div[1]//div[1]//div[1]")))

driver.quit()