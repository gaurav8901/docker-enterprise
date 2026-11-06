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


@pytest.mark.ui
def test_browser_utility_methods(driver):

    home_page = HomePage(driver)

    # Open homepage
    home_page.open_homepage()

    # Wait until document is completely loaded
    home_page.wait_for_page_load()

    # Validate JavaScript execution
    ready_state = home_page.execute_javascript(
        "return document.readyState"
    )

    assert ready_state == "complete"

    # Scroll to bottom
    home_page.scroll_to_bottom()

    # Scroll back to top
    home_page.scroll_to_top()

    scroll_position = home_page.execute_javascript(
        "return window.scrollY"
    )

    assert scroll_position == 0

    # Refresh browser
    home_page.refresh_page()

    home_page.wait_for_page_load()

    assert "practicesoftwaretesting.com" in (
        home_page.get_current_url()
    )