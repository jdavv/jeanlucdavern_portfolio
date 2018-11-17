import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


class TestSiteTitle:
    
    @pytest.fixture
    def driver_setup(self):

        mobile_emulation = {"deviceName": "iPhone 6/7/8 Plus"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation",
                                               mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)

        yield self.driver

        self.driver.quit()

    def test_site_is_reachable(self, driver_setup):
        self.driver.get('http://127.0.0.1:8000')
        assert 'jeanlucdavern.com' == self.driver.title
