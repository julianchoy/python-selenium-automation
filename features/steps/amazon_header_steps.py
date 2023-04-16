from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Hover over New Arrivals')
def hover_fashion_new_arrivals(context):
    context.app.header.hover_fashion_new_arrivals()


@then('Verify deals are visible')
def new_arrivals_deals_visible(context):
    context.app.header.new_arrivals_deals_visible()
