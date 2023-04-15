from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignIn(Page):

    def verify_signin_opened(self, verify_signin):
        self.verify_url_contains_query(verify_signin)