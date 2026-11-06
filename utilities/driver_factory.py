from selenium import webdriver

from config.settings import BROWSER, HEADLESS


class DriverFactory:

    @staticmethod
    def create_driver():

        if BROWSER == "chrome":

            options = webdriver.ChromeOptions()

            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-notifications")

            if HEADLESS:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")

            driver = webdriver.Chrome(options=options)

            return driver

        raise ValueError(
            f"Unsupported browser: {BROWSER}"
        )