from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import EXPLICIT_WAIT_SECONDS

class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            self.driver,
            EXPLICIT_WAIT_SECONDS
        )

    def open(self, url):
        self.driver.get(url)

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_visible(locator)

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_visible(locator)

        return element.text

    def is_visible(self, locator):
        try:
            self.wait_for_visible(locator)
            return True

        except Exception:
            return False

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url