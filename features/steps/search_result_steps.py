from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from pages.search_results_page import SearchResultsPage

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
CLICK_FIRST_PROD = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Click on first product')
def click_first_product(context):
    # context.driver.find_element(*CLICK_FIRST_PROD).click()
    context.app.search_results_page.click_first_product()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    # [WebElement1, WebElement2, WebElement3, ..]
    print(f'Amount of products found: {len(all_products)}')
    print(all_products)

    for product in all_products:
        print(product)
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Product image is missing'

        product_tile = product.find_element(*PRODUCT_TITLE).text
        print(product_tile)
        assert product_tile, 'Product title is missing'