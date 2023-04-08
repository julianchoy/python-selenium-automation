from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

service = Service("/Users/julian.choy/Automation/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)

# 2 Practice with locators.

driver.get('https://www.amazon.com/')
sleep(2)
driver.find_element(By.ID, "nav-link-accountList").click()

# Amazon logo
if driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").is_displayed():
    print("Amazon logo located")

# Email field
if driver.find_element(By.ID, "ap_email").is_displayed():
    print("Email field located")

# Continue button
if driver.find_element(By.ID, "continue").is_displayed():
    print("Continue button located")

# Need help link
if driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]").is_displayed():
    print("Need help link located")

# Forgot your password link
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]").click()
if driver.find_element(By.XPATH, "//a[contains(text(), 'Forgot your password?')]").is_displayed():
    print("Forgot your password link located")

# Other issues with Sign-In link
if driver.find_element(By.XPATH, "//a[contains(text(), 'Other issues with Sign-In')]").is_displayed():
    print("Other issues with Sign-In link located")

# Create your Amazon account button
if driver.find_element(By.ID, "createAccountSubmit").is_displayed():
    print("Create your Amazon account button located")

# Conditions of use link
if driver.find_element(By.XPATH, "//a[contains(@href, 'desktop_footer_cou')]").is_displayed():
    print("Conditions of use link")

# Privacy Notice link
if driver.find_element(By.XPATH, "//a[contains(@href, 'desktop_footer_privacy_notice')]").is_displayed():
    print("Privacy Notice link located")

driver.quit()

# 3 Create a test case for the Sign In page using python & selenium script
service = Service("/Users/julian.choy/Automation/python-selenium-automation/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/')
driver.find_element(By.ID, "nav-orders").click()

expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]").text

assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
assert driver.find_element(By.ID, "ap_email"), 'Email field nto shown'
print('Sign in header is visible, email input field is present')

driver.quit()