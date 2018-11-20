import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from jeanlucdavern_portfolio.projects.views import ProjectDetailView, ProjectsListView


@pytest.mark.django_db
class TestViews:
    def test_project_detail(self):
        proj = mixer.blend('projects.Project')
        path = reverse('projects:detail', kwargs={'slug': proj.slug})
        request = RequestFactory().get(path)
        response = ProjectDetailView.as_view()(request, slug=proj.slug)
        assert response.status_code == 200, 'Should be status code 200'

    def test_project_list(self):
        path = reverse('projects:list')
        request = RequestFactory().get(path)
        response = ProjectsListView.as_view()(request)
        assert response.status_code == 200, 'Should be status code 200'
