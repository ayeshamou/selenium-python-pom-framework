from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

class GoogleSearchPage(BasePage):
    search_box = (By.NAME, "q")

    def open_google(self):
        self.open(config["DEFAULT"]["base_url"])

    def search(self, text):
        box = self.find(self.search_box)
        box.send_keys(text)
        box.send_keys(Keys.RETURN)
