import pytest

from pages.home_page import HomePage


@pytest.mark.ui
@pytest.mark.smoke
def test_homepage_loads(driver):

    home_page = HomePage(driver)

    home_page.open_homepage()

    assert home_page.is_homepage_loaded(), (
        "Homepage failed to load"
    )

    assert "practicesoftwaretesting.com" in (
        home_page.get_current_url()
    )

    assert home_page.get_page_title().strip() != ""