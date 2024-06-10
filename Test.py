import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver service
serv_obj = Service(r"C:\Python\Scripts\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Set an implicit wait
driver.implicitly_wait(10)

# Open the webpage
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

# Click on the login button using an explicit wait
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login2")))
login_button.click()

# Fill in the login credentials
username_field = driver.find_element(By.ID, "loginusername")
username_field.send_keys("homex")

password_field = driver.find_element(By.ID, "loginpassword")
password_field.send_keys("tom123")

# Click on the login button using an explicit wait
login_submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@onclick='logIn()']")))
login_submit_button.click()

# Wait for the carousel next button to be clickable
carousel_next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='carousel-control-next-icon']")))

# Click the element twice with a 4-second pause in between
carousel_next_button.click()
time.sleep(4)  # Pause for 4 seconds
carousel_next_button.click()

# Pause to observe the result before closing the browser
time.sleep(5)
driver.quit()
