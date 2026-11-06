from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.settings import EXPLICIT_WAIT_SECONDS

class BasePage:
    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            self.driver,
            EXPLICIT_WAIT_SECONDS
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

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def get_text(self, locator):
        element = self.wait_for_visible(locator)

        return element.text

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url
    
    def get_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def is_visible(self, locator):
        try:
            self.wait_for_visible(locator)
            return True

        except TimeoutException:
            return False

    def open(self, url):
        self.driver.get(url)

    def scroll_into_view(self, locator):
        element = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, expected_text):
        return self.wait.until(
            EC.url_contains(expected_text)
        )