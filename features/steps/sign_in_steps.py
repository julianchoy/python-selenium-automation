from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@when('Click Amazon Orders link')
def click_orders(context):
    context.app.header.click_orders()


@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    context.app.sign_in_page.verify_signin_opened('https://www.amazon.com/ap/signin')
