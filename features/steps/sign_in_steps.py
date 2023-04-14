from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

ORDERS_BTN = (By.ID, "nav-orders")


@when('Click Amazon Orders link')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'))
