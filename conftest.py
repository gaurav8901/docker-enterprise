import pytest

from utilities.driver_factory import DriverFactory


@pytest.fixture
def driver():

    browser = DriverFactory.create_driver()

    browser.implicitly_wait(0)

    yield browser

    browser.quit()