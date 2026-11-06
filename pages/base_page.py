
from selenium.webdriver.support.ui import WebDriverWait, Select
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

    # --------------------------------
    # 1. Browser Navigation
    # --------------------------------

    def open(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def navigate_back(self):
        self.driver.back()

    def navigate_forward(self):
        self.driver.forward()

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    # --------------------------------
    # 2. Element Identification
    # --------------------------------

    def find_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_text(self, locator, text):
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, text)
        )

    # --------------------------------
    # 3. Element Interactions
    # --------------------------------

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def is_visible(self, locator):
        try:
            self.wait_for_visible(locator)
            return True
        except TimeoutException:
            return False

    # --------------------------------
    # 4. Dropdown Handling
    # --------------------------------

    def select_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_visible(locator))
        dropdown.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        dropdown = Select(self.wait_for_visible(locator))
        dropdown.select_by_value(value)

    def select_by_index(self, locator, index):
        dropdown = Select(self.wait_for_visible(locator))
        dropdown.select_by_index(index)

    def get_selected_option_text(self, locator):
        dropdown = Select(self.wait_for_visible(locator))
        return dropdown.first_selected_option.text

    # --------------------------------
    # 5. JavaScript Execution
    # --------------------------------

    def execute_javascript(self, script, *args):
        return self.driver.execute_script(script, *args)

    def scroll_to_element(self, locator):
        element = self.wait_for_visible(locator)

        self.execute_javascript(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    def scroll_to_top(self):
        self.execute_javascript(
            "window.scrollTo(0, 0);"
        )

    def scroll_to_bottom(self):
        self.execute_javascript(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    # --------------------------------
    # 6. JavaScript Alert Handling
    # --------------------------------

    def wait_for_alert(self):
        return self.wait.until(EC.alert_is_present())

    def accept_alert(self):
        alert = self.wait_for_alert()
        alert_text = alert.text
        alert.accept()
        return alert_text

    def dismiss_alert(self):
        alert = self.wait_for_alert()
        alert_text = alert.text
        alert.dismiss()
        return alert_text

    def enter_alert_text(self, text):
        alert = self.wait_for_alert()
        alert.send_keys(text)

    # --------------------------------
    # 7. Page and URL Waits
    # --------------------------------

    def wait_for_url_contains(self, expected_text):
        return self.wait.until(
            EC.url_contains(expected_text)
        )

    def wait_for_title_contains(self, expected_text):
        return self.wait.until(
            EC.title_contains(expected_text)
        )

    def wait_for_page_load(self):
        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )
