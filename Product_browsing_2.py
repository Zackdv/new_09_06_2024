# Verify that product categories can be navigated successfully.

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service(r"C:\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@id='login2']").click()
driver.find_element(By.ID, "loginusername").send_keys("homex")
driver.find_element(By.ID, "loginpassword").send_keys("tom123")
driver.find_element(By.XPATH, "//button[@onclick='logIn()']").click()


time.sleep(5)

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='carousel-control-next-icon']")))

element.click()
time.sleep(4)


driver.close()