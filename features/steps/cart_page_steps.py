from behave import when, then
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
PRODUCT_PRICE = (By.CSS_SELECTOR, '.sc-item-price-block span')
EMPTY_CART_TXT = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")
CART_BTN = (By.ID, 'nav-cart')


@when('Click on cart icon')
def open_cart_page(context):
    context.driver.find_element(*CART_BTN).click()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('Verify cart has correct product and price')
def verify_product_name(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME).text
    assert context.product_name[:30] in actual_name, f'Expected {context.product_name} but got {actual_name}'

    actual_price = context.driver.find_element(*PRODUCT_PRICE).text
    assert context.product_price == actual_price, f'Expected {context.product_price} but got {actual_price}'


@then('Verify \'Your Shopping Cart is empty.\' text present')
def verify_cart_empty(context):
    assert context.driver.find_element(*EMPTY_CART_TXT).is_displayed()
