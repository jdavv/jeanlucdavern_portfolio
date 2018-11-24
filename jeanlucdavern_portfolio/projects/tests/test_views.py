import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from jeanlucdavern_portfolio.projects.views import ProjectDetailView, ProjectsListView, TechnologiesListView


@pytest.mark.django_db
class TestProjectViews:
    def test_project_detail_view(self):
        proj = mixer.blend('projects.Project')
        path = reverse('projects:detail', kwargs={'slug': proj.slug})
        request = RequestFactory().get(path)
        response = ProjectDetailView.as_view()(request, slug=proj.slug)
        assert response.status_code == 200, 'Should be status code 200'

    def test_project_list_view(self):
        path = reverse('projects:list')
        request = RequestFactory().get(path)
        response = ProjectsListView.as_view()(request)
        assert response.status_code == 200, 'Should be status code 200'

    def test_projects_by_technologies_view(self):
        tech = mixer.blend('projects.Technologies')
        path = reverse('projects:detail', kwargs={'slug': tech.slug})
        request = RequestFactory().get(path)
        response = TechnologiesListView.as_view()(request)
        assert response.status_code == 200, 'Should be status code 200'
