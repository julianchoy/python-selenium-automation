from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Amazon T&C page')
def verify_user_can_select_pattern(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_current_window(context):
    context.og_win = context.driver.current_window_handle
    print(context.og_win)


@when('Click on Amazon Privacy Notice link')
def click_privnotice_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='https://www.amazon.com/privacy']").click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    print('ALL WINDOWS: ', windows)
    context.driver.switch_to.window(windows[1])

    context.current_window = context.driver.current_window_handle
    print('\nAFTER WE SWITCHED:')
    print(context.current_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privnotice(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))


@then('User can close new window and switch back to original')
def close_switch(context):
    context.driver.close()
    context.driver.switch_to.window(context.og_win)