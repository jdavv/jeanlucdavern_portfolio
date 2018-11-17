import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


class TestNewVisitor:
    def setup_method(self):

        mobile_emulation = {"deviceName": "iPhone 6/7/8 Plus"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation",
                                               mobile_emulation)
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def teardown_method(self):
        self.driver.quit()

    def test_site_is_reachable(self):
        self.driver.get('http://127.0.0.1:8000')
        assert 'jeanlucdavern.com' == self.driver.title
