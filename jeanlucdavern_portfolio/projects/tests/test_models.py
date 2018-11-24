import pytest
from django.template.defaultfilters import slugify
from mixer.backend.django import mixer
from jeanlucdavern_portfolio.projects.models import Project, Technologies

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

    def test_technology_name_gets_slugified(self):
        tech = mixer.blend('projects.Technologies')
        assert tech.slug == slugify(tech.title), 'Slug should pre-populate from title'


class TestManyToManyModelRelation:
    @pytest.fixture
    def setup(self):
        # Create three projects
        self.gungans = Project.objects.create(title='gungans')
        self.jedi = Project.objects.create(title='jedi')
        self.sith = Project.objects.create(title='sith')

        # Create three technologies
        self.lightsaber = Technologies.objects.create(name='lightsaber')
        self.ship = Technologies.objects.create(name='ship')
        self.bomba = Technologies.objects.create(name='bomba')

        # All projects share a technologies
        self.gungans.technologies.add(self.ship)
        self.jedi.technologies.add(self.ship)
        self.sith.technologies.add(self.ship)

        # Only jedi and sith have lightsabers
        self.jedi.technologies.add(self.lightsaber)
        self.sith.technologies.add(self.lightsaber)

    def test_project_has_technology(self, setup):
        # test all projects have ship technology
        has_ships = Project.objects.filter(technologies=self.ship)
        assert list(has_ships) == [self.gungans, self.jedi, self.sith]

    def test_project_does_not_have_technology(self, setup):
        # test gungans do not have light saber
        no_lightsabers = Project.objects.filter(technologies=self.lightsaber)
        assert self.gungans not in list(no_lightsabers)
