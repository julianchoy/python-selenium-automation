from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

service = Service("/Users/julian.choy/Automation/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)

# 1 Find the most optimal locators for Create Account (Registration) page elements

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "nav-link-accountList").click()
driver.find_element(By.ID, "createAccountSubmit").click()

# Amazon logo
sleep(4)
assert driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']").is_displayed(), 'Amazon logo not found'
print("Amazon logo located")

# 'Create account' text
assert driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").is_displayed(), 'Amazon logo not found'
print("Amazon logo located")

# 'Your name' textbox
assert driver.find_element(By.CSS_SELECTOR, "#ap_customer_name"), 'Amazon logo not found'
print("Amazon logo located")

# 'Email' textbox
assert driver.find_element(By.CSS_SELECTOR, "#ap_email"), 'Amazon logo not found'
print("Amazon logo located")

# 'Password' textbox
assert driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']"), 'Amazon logo not found'
print("Amazon logo located")

# 'Passwords must be at least 6 characters' text box
assert driver.find_element(By.CSS_SELECTOR, ".a-alert-inline-info"), 'Amazon logo not found'
print("Amazon logo located")

# 'Re-enter password' textbox
assert driver.find_element(By.CSS_SELECTOR, "#ap_password_check"), 'Amazon logo not found'
print("Amazon logo located")

# 'Create your Amazon account' button
assert driver.find_element(By.CSS_SELECTOR, "#continue"), 'Amazon logo not found'
print("Amazon logo located")

# 'Conditions of Use' link
assert driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']"), 'Amazon logo not found'
print("Amazon logo located")

# 'Privacy Notice' link
assert driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']"), 'Amazon logo not found'
print("Amazon logo located")

# 'Sign in' link
assert driver.find_element(By.CSS_SELECTOR, "[href*='signin']"), 'Amazon logo not found'
print("Amazon logo located")
