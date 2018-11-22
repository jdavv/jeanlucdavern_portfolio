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


class TestTechnologiesModel:
    def test_can_create_technology_object(self):
        technology = mixer.blend('projects.Technologies')
        assert technology.pk == 1, 'Should create a Technology instance'
