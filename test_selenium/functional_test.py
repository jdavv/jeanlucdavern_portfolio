import os
from random import choice, sample
import time
import pytest
from django.template.defaultfilters import slugify
from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

SUPERUSER_USERNAME = os.environ['DJANGO_SUPERUSER_USERNAME']
SUPERUSER_PASSWORD = os.environ['DJANGO_SUPERUSER_PASSWORD']
SELENIUM_TEST_DOMAIN = os.environ['DJANGO_SELENIUM_TEST_DOMAIN']
PROJECT_KEYWORDS = ['python', 'django', 'aws']

# ## USER STORY ###

# ## THE ADMIN ###

# The admin has just pushed the final commit for their project. It's time to
# post it as the FIRST project on their portfolio.


class Project():
    def __init__(self, PROJECT_KEYWORDS):
        fake = Faker()
        self.title = fake.text(max_nb_chars=54)
        self.description = fake.text(max_nb_chars=160)
        self.repo = fake.uri()
        self.image = choice(['/salmon.jpg', '/tuna.jpg', '/shrimp.jpg', '/deluxe.jpg'])
        self.keywords = sample(PROJECT_KEYWORDS, k=2)
        self.slug = slugify(self.title)
        self.text = fake.text(max_nb_chars=1000)


class PortfolioBase():
    @pytest.fixture
    def driver_setup(self):
        # The admin points their browser at the admin login.
        mobile_emulation = {"deviceName": "iPhone 6/7/8 Plus"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation",
                                               mobile_emulation)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(f'{SELENIUM_TEST_DOMAIN}/admin/')
        # Check to make sure not already logged in.
        try:
            self.driver.find_element_by_id('user-tools')
            yield self.driver
        except NoSuchElementException:
            # Admin is not already logged in.  username = self.driver.find_element_by_id('id_username')
            # They type in their username.
            username = self.driver.find_element_by_id('id_username')
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

    def add_option(self, option):
        link = self.driver.find_element_by_id('add_id_keywords')
        link.send_keys(Keys.ENTER)
        self.driver.switch_to_window(self.driver.window_handles[1])
        keywords_name = self.driver.find_element_by_id('id_name')
        keywords_name.clear()
        keywords_name.send_keys(option)
        # The admin clicks the save button.
        keywords_save = self.driver.find_element_by_name('_save')
        keywords_save.send_keys(Keys.ENTER)
        self.driver.switch_to_window(self.driver.window_handles[0])
        return

    def create_project_with_admin_site(self, driver_setup, project):
        # The admin now points their browser to the projects admin page.
        self.driver.get(f'{SELENIUM_TEST_DOMAIN}/admin/projects/project/add/')
        # The admin sees a textbox for Title and types "Fat Salmon".
        title = self.driver.find_element_by_name('title')
        title.send_keys(project.title)
        # The admin sees a textbox for Description and types a description.
        description = self.driver.find_element_by_name('description')
        description.clear()
        description.send_keys(project.description)
        # The admin sees a textbox for Text and types a description (Should
        # allow html to be used)
        text = self.driver.find_element_by_name('text')
        text.send_keys(project.text)
        # The admin sees a textbox for Repo and types in the github reposistory
        # url.
        repo = self.driver.find_element_by_name('repo')
        repo.send_keys(project.repo)
        # The admin NOTICES a textbox under Repo called Slug. It's already filled in
        # with the text "fat-salmon"
        slug = self.driver.find_element_by_name('slug')
        slug_text = slug.get_attribute('value')
        expected = slugify(slug_text)
        # Test the slugify and Project model autofill this field.
        assert slug_text == expected, 'Slug should auto populating from title'
        # The admin sees a button labeled "Choose File". The admin clicks it and selects
        # a picture of a salmon.
        image = self.driver.find_element_by_name('image')
        cwd = os.getcwd()
        image.send_keys(f'{cwd}/test_selenium/{project.image}')
        # The admin adds relative keywords to tag their project.
        keywords_options = self.driver.find_elements_by_tag_name('option')
        # The admin checks if they keyword was already used before, its ifs in
        # the list they will click it if not add it.
        for option in keywords_options:
            if option.text in project.keywords:
                option.click()
        for keyword in project.keywords:
            if keyword not in [option.text for option in keywords_options]:
                self.add_option(keyword)
        project_save = self.driver.find_element_by_name('_save')
        project_save.send_keys(Keys.ENTER)


class TestAdminCreatesProjects(PortfolioBase):

    @pytest.fixture
    def creates_project(self, driver_setup):
        self.proj = Project(PROJECT_KEYWORDS)
        self.create_project_with_admin_site(driver_setup, self.proj)
        yield self.proj

    def test_project_is_shown_in_list_view(self, driver_setup, creates_project):
        self.driver.get(f'{SELENIUM_TEST_DOMAIN}/projects/')
        elements = self.driver.find_elements_by_id('project_title')
        titles = [element.text for element in elements]
        expected = self.proj.title
        assert expected in titles, 'All projects should display title on this page'

    def test_project_detail_view(self, driver_setup, creates_project):
        self.driver.get(f'{SELENIUM_TEST_DOMAIN}/projects/{self.proj.slug}')
        assert 1
