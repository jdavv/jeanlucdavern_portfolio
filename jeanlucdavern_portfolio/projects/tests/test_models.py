import pytest
from django.template.defaultfilters import slugify
from mixer.backend.django import mixer
from jeanlucdavern_portfolio.projects.models import Project

pytestmark = pytest.mark.django_db


class TestModels:
    def test_get_string_repr(self):
        project = Project(title="this title")
        assert str(project) == "this title"

    def test_model(self):
        obj = mixer.blend('projects.Project')
        assert obj.pk == 1, 'Should create a Project instance'

    def test_project_title_is_slugified(self):
        proj = mixer.blend('projects.Project')
        assert proj.slug == slugify(proj.title), 'Slug should pre-populate from title'
