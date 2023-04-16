from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def open_product_id(self, product_id):
        self.open_url(f'https://www.amazon.com/dp/{product_id}/')
