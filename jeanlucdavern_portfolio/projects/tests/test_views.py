from django.test import RequestFactory, TestCase
from django.urls import reverse
from jeanlucdavern_portfolio.projects.views import ProjectsListView, ProjectDetailView
from jeanlucdavern_portfolio.projects.models import Project
import pytest


@pytest.mark.django_db
class TestViews:
    def test_project_detail(self):
        self.project = Project.objects.create(
            title='title',
            description='description is descriptive',
            repo='http://test.com')
        path = reverse('projects:detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)

        response = ProjectDetailView.as_view()(request, pk=1)
        assert response.status_code == 200
