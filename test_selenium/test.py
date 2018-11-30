import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from faker import Faker
from django.test import LiveServerTestCase
import os
from pathlib import Path

SUPERUSER_USERNAME = os.environ['DJANGO_SUPERUSER_USERNAME']
SUPERUSER_PASSWORD = os.environ['DJANGO_SUPERUSER_PASSWORD']
# ## USER STORY ###


# ## THE ADMIN ###

# The admin has just pushed the final commit for their project. It's time to
# post it as the FIRST project on their portfolio.


class TestAdminCreatesProject():
    @pytest.fixture
    def driver_setup(self):
        # The admin points their browser at the admin login.
        mobile_emulation = {"deviceName": "iPhone 6/7/8 Plus"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation",
                                               mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://127.0.0.1:8000/admin/')
        # Check to make sure not already logged in.
        try:
            self.driver.find_element_by_id('user-tools')
            yield self.driver
        except NoSuchElementException:
            # Admin is not already logged in.
            username = self.driver.find_element_by_id('id_username')
            # They type in their username.
            username.send_keys(SUPERUSER_USERNAME)
            password = self.driver.find_element_by_id('id_password')
            # Then they type in their password.
            password.send_keys(SUPERUSER_PASSWORD)
            password.send_keys(Keys.TAB)
            password.send_keys(Keys.ENTER)
            # The admin is now logged in and on the Django administration
            # panel.
            yield self.driver
        self.driver.quit()

    def test_admin_creates_fat_salmon_project(self, driver_setup):
        # The admin now points their browser to the projects admin page.
        self.driver.get('http://127.0.0.1:8000/admin/projects/project/add/')
        # The admin sees a textbox for Title and types "Fat Salmon".
        title = self.driver.find_element_by_name('title')
        title.send_keys('Fat Salmon')
        # The admin sees a textbox for Description and types a description.
        description = self.driver.find_element_by_name('description')
        description.send_keys(
            'Salmon is the common name for several species of ray-finned fish in the family Salmonidae'
        )

        # The admin sees a textbox for Repo and types in the github reposistory
        # url.
        repo = self.driver.find_element_by_name('repo')
        repo.send_keys('https://github.com/jdavv/fat-salmon')
        # The admin NOTICES a textbox under Repo called Slug. It's already filled in
        # with the text "fat-salmon"
        slug = self.driver.find_element_by_name('slug')
        slug_text = slug.get_attribute('value')
        # Test the slugify and Project model autofill this field.
        assert slug_text == 'fat-salmon', 'Slug should auto populating from title'
        # The admin sees a button labeled "Choose File". The admin clicks it and selects
        # a picture of a salmon.
        image = self.driver.find_element_by_name('image')
        image.send_keys(os.getcwd() + '/salmon.jpg')
        # image.send_keys(str(Path(__file__).resolve().parent)) + '/salmon.jpg'
        # The admin notices Keywords box is empty and clicks the plus button to
        # add a keyword.
        keywords = self.driver.find_element_by_name('keywords')
        keywords_options = [
            keyword for keyword in keywords.find_elements_by_tag_name('option')
        ]
        # Check no keywords exists.
        assert len(keywords_options) == 0, 'Should be first entry to database'

        link = self.driver.find_element_by_id('add_id_keywords')
        link.send_keys(Keys.ENTER)
        # The admin sees their browser opened a new window.
        self.driver.switch_to_window(self.driver.window_handles[1])
        # The admin sees a text box for name, they type in "python".
        keywords_name = self.driver.find_element_by_id('id_name')
        keywords_name.send_keys('python')
        # The admin clicks the save button.
        keywords_save = self.driver.find_element_by_name('_save')
        keywords_save.send_keys(Keys.ENTER)
        # The window closed and now the admin is back where they started.
        self.driver.switch_to_window(self.driver.window_handles[0])
        # The admin, satisfied with what they have filled in clicks save.
        project_save = self.driver.find_element_by_name('_save')
        project_save.send_keys(Keys.ENTER)
