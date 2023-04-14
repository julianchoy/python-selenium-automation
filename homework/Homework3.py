from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

service = Service("/Users/julian.choy/Automation/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.wait = WebDriverWait(driver, 10)

# 1 Find the most optimal locators for Create Account (Registration) page elements

driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "nav-link-accountList").click()
driver.find_element(By.ID, "createAccountSubmit").click()

# Amazon logo
driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[aria-label='Amazon']")))
assert driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']").is_displayed(), 'Amazon logo not found'
print("Amazon logo located")

# 'Create account' text
assert driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").is_displayed(), 'Create account text not found'
print("Create account text located")

# 'Your name' textbox
assert driver.find_element(By.CSS_SELECTOR, "#ap_customer_name"), 'Your name textbox not found'
print("Your name textbox located")

# 'Email' textbox
assert driver.find_element(By.CSS_SELECTOR, "#ap_email"), 'Email textbox not found'
print("Email textbox located")

# 'Password' textbox
assert driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']"), 'Password textbox not found'
print("Password textbox located")

# 'Passwords must be at least 6 characters' text box
assert driver.find_element(By.CSS_SELECTOR, ".a-alert-inline-info"), 'Passwords must be at least 6 characters text box not found'
print("Passwords must be at least 6 characters text box located")

# 'Re-enter password' textbox
assert driver.find_element(By.CSS_SELECTOR, "#ap_password_check"), 'Re-enter password textbox not found'
print("Re-enter password textbox located")

# 'Create your Amazon account' button
assert driver.find_element(By.CSS_SELECTOR, "#continue"), 'Create your Amazon account button not found'
print("Create your Amazon account button located")

# 'Conditions of Use' link
assert driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']"), 'Conditions of Use link not found'
print("Conditions of Use link located")

# 'Privacy Notice' link
assert driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']"), 'Privacy Notice link not found'
print("Privacy Notice' link located")

# 'Sign in' link
assert driver.find_element(By.CSS_SELECTOR, "[href*='signin']"), 'Sign in link not found'
print("Sign in link located")
