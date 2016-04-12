"""
Parallel testing with Selenium Grid and pytest.
"""
import pytest
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(30)
    selenium.maximize_window()
    return selenium


def test_one(selenium):
    try:
        selenium.get("http://www.python.org")
        assert "Python" in selenium.title
        elem = selenium.find_element_by_name("q")
        elem.send_keys("documentation")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in selenium.page_source
    finally:
        pass


def test_two(selenium):
    try:
        selenium.get("http://www.google.com")
        elem = selenium.find_element_by_name("q")
        elem.send_keys("webdriver")
        elem.send_keys(Keys.RETURN)
    finally:
        pass
