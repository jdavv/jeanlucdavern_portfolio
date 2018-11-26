import pytest
from django.template.defaultfilters import slugify
from mixer.backend.django import mixer

from jeanlucdavern_portfolio.projects.models import Project

pytestmark = pytest.mark.django_db


class TestProjectsModel:
    def test_get_string_repr(self):
        project = Project(title="this title")
        assert str(project) == "this title"

    def test_can_create_project_object(self):
        obj = mixer.blend('projects.Project')
        assert obj.pk == 1, 'Should create a Project instance'

    def test_project_title_is_slugified(self):
        proj = mixer.blend('projects.Project')
        assert proj.slug == slugify(proj.title), 'Slug should pre-populate from title'

    def test_get_absolute_url(self):
        proj = mixer.blend('projects.Project')
        assert proj.get_absolute_url() == f'/projects/{proj.slug}/', 'Should fail if urlconf is not defined correctly'


class TestKeywordsModel:
    def test_can_create_keywords_object(self):
        keyword = mixer.blend('projects.Keywords')
        assert keyword.pk == 1, 'Should create a Keywords instance'

    def test_keywords_name_gets_slugified(self):
        keyword = mixer.blend('projects.Keywords')
        assert keyword.slug == slugify(keyword.name), 'Slug should pre-populate from name'

    def test_str_is_slug(self):
        keyword = mixer.blend('projects.Keywords')
        assert str(keyword) == slugify(keyword.name), '__str__ should pre-populate from name'

    def test_get_absolute_url(self):
        keyword = mixer.blend('projects.Keywords')
        assert keyword.get_absolute_url() == f'/projects/tagged/{keyword.slug}/', 'Should fail if urlconf is not defined'
