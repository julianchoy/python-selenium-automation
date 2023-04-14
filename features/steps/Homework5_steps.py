from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

PINEAPPLE_OPTIONS = (By.CSS_SELECTOR, "#tp-inline-twister-dim-values-container li[data-asin]")
CURRENT_PINEAPPLE = (By.ID, "inline-twister-expanded-dimension-text-color_name")


@then('Verify user can click through pattern')
def verify_user_can_select_pattern(context):
    context.driver.find_element(*PINEAPPLE_OPTIONS).click()  # click on 1

    all_color_options = context.driver.find_elements(*PINEAPPLE_OPTIONS)

    actual_colors = []
    for color in all_color_options:
        color.click()
        current_color = context.driver.find_element(*CURRENT_PINEAPPLE).text
        print('Current color: ', current_color)
        actual_colors += [current_color]
