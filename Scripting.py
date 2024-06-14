from modulefinder import Module

import select
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import by, By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Assuming you are using Chrome, you need to have chromedriver installed and in PATH

# Navigate to the URL
driver.get('https://google.com')
# time.sleep(10)
# driver.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys('Paralex Bank')
# time.sleep(5)
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/*[name()='svg'][1]").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/ul[1]/li[3]/div[1]/div[2]/div[1]/div[1]/span[1]/b[2]").click()
# time.sleep(30)


# # Enter Password and Username
# Enter_Username = driver.find_element(By.XPATH, "username")
# Enter_Username.send_keys("Admin")
# time.sleep(1)
# Enter_Password = driver.find_element(By.NAME, "password")
# Enter_Password.send_keys("admin123")
# time.sleep(1)
# Click_Login = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
# Click_Login.click()
# time.sleep(5)