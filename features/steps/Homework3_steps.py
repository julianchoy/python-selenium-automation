from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon Page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)


@when('Click on Orders')
def click_order_button(context):
    context.driver.find_element(By.ID, "nav-orders").click()


@then('Verify Sign In is visible')
def sign_in_visible(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small"), 'Sign in not visible'
    print('Sign in visible')


@then('Verify Email input field is present')
def sign_in_visible(context):
    assert context.driver.find_element(By.ID, "ap_email"), 'Email input field is not present'
    print('Email input field is present')