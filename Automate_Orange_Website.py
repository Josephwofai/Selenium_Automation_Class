from selenium import webdriver
import driver as driver
from selenium.webdriver.common.by import by, By
import time




# Initialize the WebDriver
driver = webdriver.Chrome()  # Assuming you are using Chrome, you need to have chromedriver installed and in PATH

# Navigate to the URL
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)

# Enter Password and Username
Enter_Username = driver.find_element(By.NAME, "username")
Enter_Username.send_keys("Admin")
time.sleep(1)
Enter_Password = driver.find_element(By.NAME, "password")
Enter_Password.send_keys("admin123")
time.sleep(1)
Click_Login = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
Click_Login.click()
time.sleep(3)
# Admin module
# Click_Admin = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > '
#                                                    'div.oxd-sidepanel-body > ul > li:nth-child(1) > a > span')
# Click_Admin.click()
# time.sleep(2)
# PIM Module
# Click_PIM = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1) > span:nth-child(2)')
# Click_PIM.click()
# time.sleep(2)

# Leave module
Click_Leave = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > '
                                                   'aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > '
                                                   'ul:nth-child(2) > li:nth-child(3) > a:nth-child(1) > '
                                                   'span:nth-child(2)')
Click_Leave.click()
time.sleep(2)
# Select From date
driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div '
                                     '> div.oxd-table-filter > div.oxd-table-filter-area > form > div:nth-child(1) > '
                                     'div > div:nth-child(1) > div > div:nth-child(2) > div > div > '
                                     'input').send_keys('2023-20-04')
# time.sleep(1)
# Select To Date
driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div '
                                     '> div.oxd-table-filter > div.oxd-table-filter-area > form > div:nth-child(1) > '
                                     'div > div:nth-child(2) > div > div:nth-child(2) > div > div > '
                                    'input').send_keys('2023-05-05')
time.sleep(2)

# Enter EmployeesName
driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div '
                                     '> div.oxd-table-filter > div.oxd-table-filter-area > form > div:nth-child(2) > '
                                     'div > div:nth-child(1) > div > div:nth-child(2) > div > div > input').send_keys('Manda')

driver.find_element(By.CSS_SELECTOR, '.oxd-switch-input.oxd-switch-input--active.--label-right').click()
time.sleep(2)



# # Select_LS
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div['
#                               '2]/div/div[1]/div[1]').send_keys('Rejected')

# driver.find_element(By.XPATH, '//*[@id="app"]//form//div[contains(@class, "some-class")]//div[contains(@class, '
#                               '"another-class")]//input').send_keys('Rejected')
time.sleep(2)
# # JOB DROPDOWN
# Click_JOB = driver.find_element(By.CSS_SELECTOR, '/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul['
#                                                  '1]/li[2]/span[1]').click()
time.sleep(5)
