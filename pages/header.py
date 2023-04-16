from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    ORDERS_BTN = (By.ID, "nav-orders")
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    CART_BTN = (By.ID, 'nav-cart-count')
    LANG_OPTIONS = (By.ID, 'icp-nav-flyout')
    SPANISH_LANG = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    FASHION_NEW_ARRIVALS_HOVER = (By.CSS_SELECTOR, "[aria-label='New Arrivals']")
    NEW_ARRIVALS_DEALS = (By.XPATH, "//li[contains(text(),'See More')]")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_cart(self):
        self.click(*self.CART_BTN)

    def hover_lang_options(self):
        lang_options = self.find_element(*self.LANG_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def verify_lang_shown(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')

    def hover_fashion_new_arrivals(self):
        lang_options = self.find_element(*self.FASHION_NEW_ARRIVALS_HOVER)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang_options)
        actions.perform()

    def new_arrivals_deals_visible(self):
        self.wait_for_element_appear(*self.NEW_ARRIVALS_DEALS)
