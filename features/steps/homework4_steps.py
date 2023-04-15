from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage

CLICK_FIRST_PROD = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-button")


@given('Open Amazon Best Sellers page')
def open_amazon_bestsellers(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


# @when('Click on first product')
# def click_first_product(context):
#     context.driver.find_element(*CLICK_FIRST_PROD).click()


# @when('Click on Add to Cart')
# def click_add_to_cart(context):
#     # context.driver.find_element(*ADD_TO_CART).click()
#     context.app.product_page.click_add_to_cart()


@then('Verify that Best Sellers tab has {expected_value} links')
def verify_links_displayed(context, expected_value):
    bs_links = context.driver.find_elements(By.CSS_SELECTOR, "#zg_header a")
    assert len(bs_links) == 5, f'Expected {expected_value} but got {bs_links}'


# @then('Verify that cart has {cart_value} item')
# def verify_cart(context, cart_value):
#     actual_value = context.driver.find_element(By.CSS_SELECTOR, "#nav-cart-count").text
#     assert actual_value == cart_value, f'Expected {cart_value} but got {actual_value}'
