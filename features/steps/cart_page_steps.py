from behave import when, then
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
PRODUCT_PRICE = (By.CSS_SELECTOR, '.sc-item-price-block span')
EMPTY_CART_TXT = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")
CART_BTN = (By.ID, 'nav-cart')


@when('Click on cart icon')
def open_cart_page(context):
    context.app.header.click_cart()


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


@then('Verify {expected_text} text present')
def verify_cart_empty_txt(context, expected_text):
    context.app.cart_page.verify_empty_cart_msg(expected_text)


@then('Verify that cart has {cart_value} item')
def verify_cart(context, cart_value):
    context.app.cart_page.verify_cart_value(cart_value)
    # actual_value = context.driver.find_element(By.CSS_SELECTOR, "#nav-cart-count").text
    # assert actual_value == cart_value, f'Expected {cart_value} but got {actual_value}'
