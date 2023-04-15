from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ACTUAL_CART_VALUE = (By.CSS_SELECTOR, "#nav-cart-count")
    EMPTY_CART_TXT = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart is empty')]")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_cart_value(self, cart_value):
        self.verify_text(cart_value, *self.ACTUAL_CART_VALUE)

    def verify_empty_cart_msg(self, cart_value):
        self.verify_text(cart_value, *self.EMPTY_CART_TXT)
