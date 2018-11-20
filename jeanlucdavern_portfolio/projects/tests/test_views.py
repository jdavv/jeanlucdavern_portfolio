from django.test import RequestFactory, TestCase
from django.urls import reverse
from jeanlucdavern_portfolio.projects.views import ProjectsListView, ProjectDetailView
from jeanlucdavern_portfolio.projects.models import Project
import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViews:
    def test_project_detail(self):
        proj = mixer.blend('projects.Project')
        path = reverse('projects:detail', kwargs={'pk': 1})
        request = RequestFactory().get(path)
        response = ProjectDetailView.as_view()(request, pk=proj.pk)
        assert response.status_code == 200

    def test_project_list(self):
        path = reverse('projects:list')
        request = RequestFactory().get(path)
        response = ProjectsListView.as_view()(request)
        assert response.status_code == 200
