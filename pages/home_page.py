from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config.settings import BASE_URL


class HomePage(BasePage):

    BODY = (By.TAG_NAME, "body")

    def open_homepage(self):

        self.open(BASE_URL)

    def is_homepage_loaded(self):

        body = self.wait_for_visible(self.BODY)

        return bool(body.text.strip())