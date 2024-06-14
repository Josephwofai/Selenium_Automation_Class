from modulefinder import Module

import select
from selenium import webdriver
import driver as driver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
# Navigate to the URL
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)
driver.maximize_window()

# Enter Password and Username
Enter_Username = driver.find_element(By.NAME, "username")
Enter_Username.send_keys("Admin")
# time.sleep()
Enter_Password = driver.find_element(By.NAME, "password")
Enter_Password.send_keys("admin123")
# time.sleep()
Click_Login = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
Click_Login.click()
time.sleep(3)
#
# # Admin_Module...............................
Click_Admin = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > '
                                                   'div.oxd-sidepanel-body > ul > li:nth-child(1) > a > span')
Click_Admin.click()
time.sleep(2)

# User_Managements...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
time.sleep(3)
# Job...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
time.sleep(3)
# Organizations...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click()
time.sleep(3)
# Qualification...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click()
time.sleep(3)
# Nationalities...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a").click()
time.sleep(3)
# Corporate Branding...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a").click()
time.sleep(3)
# Configuration...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span").click()
time.sleep(4)
#
#
# PIM_Module..............................................
Click_PIM = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
Click_PIM.click()
time.sleep(3)
# Configuration...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
time.sleep(3)
# Employee_list
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
time.sleep(3)
# Add_Employee
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
time.sleep(3)
# Reports
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click()
time.sleep(3)
#
#
# Leave_Module........................................
Click_Leave = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')
Click_Leave.click()
time.sleep(2)
# Apply...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
time.sleep(3)
# My Leave
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
time.sleep(3)
# Entitlement
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click()
time.sleep(3)
# Reports
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click()
time.sleep(2)
# Configure
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/span").click()
time.sleep(3)
# Leave list
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a").click()
time.sleep(3)
# Assign Leave
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/a").click()
time.sleep(3)
#

# Time_Module........................................
Click_Time = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li['
                                           '4]/a[1]/span[1]')
Click_Time.click()
time.sleep(3)
# Timesheet...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
time.sleep(3)
# Attendance...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
time.sleep(3)
# Reports...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click()
time.sleep(3)
# Project_Info
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span").click()
time.sleep(3)


# Recruitment_Module........................................
Click_Recruitment = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
Click_Recruitment.click()
time.sleep(3)
# Candidates...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/a").click()
time.sleep(3)
# Vacancies...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
time.sleep(3)
#
# My_Info..................................
Click_My_Info = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span')
Click_My_Info.click()
time.sleep(3)
# Personal_Details...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a").click()
time.sleep(3)
# Contact_Details...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a").click()
time.sleep(3)
# Emergency_Contact...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a").click()
time.sleep(3)
# Dependents...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a").click()
time.sleep(3)
# Immigration...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a").click()
time.sleep(3)
# Job...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a").click()
time.sleep(3)
# Salary...
driver.find_element(By.XPATH, "//html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a").click()
time.sleep(3)
# Report_To...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a").click()
time.sleep(3)
# Qualification...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a").click()
time.sleep(3)
# Membership...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a").click()
time.sleep(3)

# Performance..................................
Click_Performance = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
Click_Performance.click()
time.sleep(3)
# Configure...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span").click()
time.sleep(3)
# Manage_review...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
time.sleep(3)
# My_Tracker...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a").click()
time.sleep(3)
# Employee_Tracker...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a').click()
time.sleep(4)
#
#
# # Dash_Board..................................
Click_Dash_Board = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span')
Click_Dash_Board.click()
time.sleep(2)
# John Doe...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
time.sleep(4)
# About...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[1]/a").click()
time.sleep(10)
# Close_About
driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/button").click()
time.sleep(6)

# John Doe
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
time.sleep(2)
# Support
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[2]/a").click()
time.sleep(6)
# John Doe
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
time.sleep(3)

# Change_Password
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[3]/a").click()
time.sleep(3)
# Cancel..
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]').click()
time.sleep(3)
#
#
# Directory..................................
Click_Directory = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span')
Click_Directory.click()
time.sleep(2)
# Employee_Name
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div['
                              '2]/div/div/input').send_keys('Doe John')
time.sleep(3)
# V_ Button...
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]").click()
time.sleep(3)
# Records...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[5]/div').click()
time.sleep(4)

# # Logout...................
# driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
# time.sleep(3)
#
# Click_Logout = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
# Click_Logout.click()
# time.sleep(3)


#
# Maintenance..................................
Click_Maintenance = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span')
Click_Maintenance.click()
time.sleep(5)
# Password..
Enter_Password = driver.find_element(By.NAME, "password")
Enter_Password.send_keys("QQQ")
time.sleep(3)
# Confirm...
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]').click()
time.sleep(3)
# Cancel..
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/form/div[5]/button[1]").click()
time.sleep(3)



# Claim.........................
Click_Claim = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a')
Click_Claim.click()
time.sleep(2)
# # Configure
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span').click()
time.sleep(3)
# Submit Claim..
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
time.sleep(3)
# My Claim...
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
time.sleep(3)
# Employee Claim..
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/a").click()
time.sleep(3)
# Assign Claim...
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a').click()
time.sleep(3)

#
#
#
# # Buzz.......................
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul['
                              '1]/li[12]/a[1]/span[1]').click()
time.sleep(3)
# # Buzz Newsfeed-POST
Post = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div['
                                     '2]/form/div/textarea')
Post.send_keys("Good Bye Team Automation-Python-Selenium")
time.sleep(10)
# Post Button..
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div[1]/div['
                              '2]/form/div/div/button').click()
time.sleep(5)
# Hand Bugger..
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div['
                              '2]/li/button').click()
time.sleep(5)
# Hand Bugger..
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div['
                              '2]/li/button').click()
time.sleep(5)
# Delete Post
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div['
                              '2]/li/ul/li[1]/p').click()
time.sleep(4)
# No Cancel..
driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]').click()
time.sleep(4)
# Hand Bugger..
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div['
                              '2]/li/button').click()
time.sleep(4)
# Edit Post
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div['
                              '2]/li/ul/li[2]/p').click()
# Clear
driver.find_element(By.XPATH, '//html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div['
                              '1]/form[1]/div[1]/div[2]/div[1]/textarea[1]').clear()
time.sleep(8)
# Close..
driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/div/div/button').click()
time.sleep(3)
#


# Logout...................
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p").click()
time.sleep(3)

Click_Logout = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
Click_Logout.click()
time.sleep(3)


















































# # Employee name..
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input').send_keys('Doctor Doe Emmy')
# time.sleep(3)
# # Create Button...
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]').click()
# time.sleep(3)
# # Cancel...
# driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[1]').click()
# time.sleep(10)


# # Leave module
# Click_Leave = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > '
#                                                    'aside:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > '
#                                                    'ul:nth-child(2) > li:nth-child(3) > a:nth-child(1) > '
#                                                    'span:nth-child(2)')
# Click_Leave.click()
# time.sleep(2)
#
#
# # # Select From date/Click Clear
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div['
#                                      '1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]').click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '.oxd-date-input-link.--clear').click()
# time.sleep(2)
# #
# # driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div['
# #                                      '1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]').send_keys('2024-24-05')
# # time.sleep(2)
# # # # Select To date/Click Clear;# # driver.find_element(By.CSS_SELECTOR, 'iv[class="oxd-table-filter"] div:nth-child(1) div:nth-child(1) div:nth-child('
# #                                      '1) div:nth-child(1) div:nth-child(2) div:nth-child(1) div:nth-child(1) '
# #                                      'input:nth-child(1)').click()
# # time.sleep(2)
# #
# # driver.find_element()
# #
# # driver.find_element(By.CSS_SELECTOR, 'div[class="oxd-table-filter"] div:nth-child(1) div:nth-child(1) div:nth-child('
# #                                      '1) div:nth-child(1) div:nth-child(2) div:nth-child(1) div:nth-child(1) '
# #                                      'input:nth-child(1)').send_keys('2024-30-05')
# # time.sleep(2)
#
#
# # Enter EmployeesName
# driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div '
#                                      '> div.oxd-table-filter > div.oxd-table-filter-area > form > div:nth-child(2) > '
#                                      'div > div:nth-child(1) > div > div:nth-child(2) > div > div > input').send_keys('Manda')
#
# Include_Past_Employees = driver.find_element(By.CLASS, '[Class ="oxd-switch-input oxd-switch-input--active '
#                                                          '--label-right"]')
# Include_Past_Employees.click()
# time.sleep(2)
#
# # # Select_LS
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div['
#                               '2]/div/div[1]/div[1]').send_keys('Rejected')
#
# driver.find_element(By.XPATH, '//*[@id="app"]//form//div[contains(@class, "some-class")]//div[contains(@class, '
#                               '"another-class")]//input').send_keys('Rejected')
# time.sleep(2)
#
# # # JOB DROPDOWN
# Click_JOB = driver.find_element(By.CSS_SELECTOR, '/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul['
#                                                  '1]/li[2]/span[1]').click()
# time.sleep(5)
#
# # Apply_Leave
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/a[1]').click()
# time.sleep(1)
#
# # # # Click_MyLeave
# driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]").click()
# time.sleep(3)
#
# # Click_Entitlement:Employee Entitlement
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span').click()
# time.sleep(3)
#
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]/a').click()
# time.sleep(3)
# #
# # # Click_Leave_Reports: Leave Entitlements and Usage Report
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a').click()
# time.sleep(2)
# #
# # # Click_Configure: Holidays
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/span').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[1]/a').click()
# time.sleep(1)
#
# # # Click_Leave List
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[1]').click()
# time.sleep(2)
# # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/span/text()').click()
#
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input').send_keys('John Doe')
# time.sleep(2)
# # # Pending Approval
# # # Click_Assign Leave
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/ul/div[2]/li/a').click()
# time.sleep(2)


# Select Employee
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div['
#                                      '2]/div[1]/div[3]/div[1]/label[1]/span[1]').click()
# time.sleep(2)
# #
# # # Search/Reset Button
# driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
# #
# #
# # # Date Tick Button
# # driver.find_element(By.CSS_SELECTOR, '.oxd-icon.bi-check.oxd-checkbox-input-icon').click()
# # time.sleep(2)
#
#
# # Recruitment Menu
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, 'li[class="oxd-topbar-body-nav-tab --visited"] a['
#                                      'class="oxd-topbar-body-nav-tab-item"]').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child('
#                                      '2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) '
#                                      '> div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(7) > '
#                                      'div:nth-child(1) > button:nth-child(1) > i:nth-child(1)').click()
# time.sleep(2)
#
# # # # Candidate AddNew functionality..........................................
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/a[1]').click()
# time.sleep(3)
# #
# # # AddNew..
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/button[1]').click()
# time.sleep(2)
# #
# # # AddCandidate..FN,MN,LN
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]').send_keys('Water')
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Middle Name"]').send_keys('Zion')
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]').send_keys('Ella')
# time.sleep(3)
# #
# # # Email..
# driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child('
#                                      '2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) '
#                                      '> div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > '
#                                      'input:nth-child(1)').send_keys('123qwe@gmail.com')
# # # Contact Number..
# driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child('
#                                      '2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) '
#                                      '> div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > '
#                                      'input:nth-child(1)').click()
# # time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, '.oxd-date-input-link.--clear').click()
#
# driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child('
#                                      '2) > div:nth-child(1) > div:nth-child(1) > form:nth-child(3) > div:nth-child(3) '
#                                      '> div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > '
#                                      'input:nth-child(1)').send_keys('123456789')
# # # Keywords..
# # driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/div['
# #                               '1]/div[1]/div[2]/input[1]').send_keys('I love God')
# #
# # # Date of App...
# # # driver.find_element(By.CSS_SELECTOR, 'input[placeholder="yyyy-dd-mm"]').send_keys('2024-07-05')
# # # time.sleep(5)
# # # Check Box..
# # driver.find_element(By.CSS_SELECTOR, '.oxd-icon.bi-check.oxd-checkbox-input-icon').click()
# # time.sleep(3)
# # # save..
# # driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div['
# #                                      '8]/button[2]').click()
# # time.sleep(3)
# # driver.quit()
#
#
# #
# # # Recruitment Vacancy..............................................
# # # Vacancy
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[2]/a[1]').click()
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,
#                     'div[class="oxd-grid-4 orangehrm-full-width-grid"] div:nth-child(1) div:nth-child(1) '
#                     'div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)').click()
# # # time.sleep(3)
# # # # Job Title..
# # driver.find_element(By.CLASS_NAME, 'oxd-select-text-input').click()
# # time.sleep(5)
# #
# # # Vacancy sub..
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div['
#                                      '1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/i[1]').click()
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, 'oxd-select-text-input').send_keys('Test')
# time.sleep(5)
# Hiring Manager..
# driver.find_element(By.CLASS_NAME, 'oxd-select-text-input')
# time.sleep(15)


#
# driver.find_element(By.CLASS_NAME, 'oxd-icon bi-dash oxd-checkbox-input-icon').click()
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
# time.sleep(5)
#
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div['
#                               '1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]').click()
# time.sleep(5)
#
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[1]').click()
# time.sleep(3)
