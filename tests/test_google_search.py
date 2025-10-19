import time
from pages.google_search_page import GoogleSearchPage

def test_google_search(setup_driver):
    driver = setup_driver
    google_page = GoogleSearchPage(driver)

    google_page.open_google()
    google_page.search("Selenium Python")

    time.sleep(3)
    assert "Selenium" in google_page.get_title(), "Search results not displayed!"
    print("✅ Test Passed: Google Search via POM successful!")
