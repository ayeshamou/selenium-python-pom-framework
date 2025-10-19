import pytest
from utils.browser_setup import get_driver

@pytest.fixture
def setup_driver():
    driver = get_driver()
    yield driver
    driver.quit()
