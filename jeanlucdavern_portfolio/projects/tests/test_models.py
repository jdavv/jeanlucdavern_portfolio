import pytest

from jeanlucdavern_portfolio.projects.models import Project

pytestmark = pytest.mark.django_db


class TestModels:
    def test_get_string_repr(self):
        project = Project(title="this title")
        assert str(project) == "this title"
