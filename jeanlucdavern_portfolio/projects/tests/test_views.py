import pytest
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
from ..models import Project
from jeanlucdavern_portfolio.projects.views import (
    ProjectDetailView, ProjectsListView,
    ProjectsUsingTheseKeywordsListView)


@pytest.mark.django_db
class TestProjectViews:
    def test_project_detail_view(self):
        self.proj = mixer.blend('projects.Project')
        self.path = reverse('projects:detail', kwargs={'slug': self.proj.slug})
        self.request = RequestFactory().get(self.path)
        self.response = ProjectDetailView.as_view()(self.request, slug=self.proj.slug)
        assert self.response.status_code == 200, 'Should be status code 200'

    def test_project_list_view(self):
        self.path = reverse('projects:list')
        self.request = RequestFactory().get(self.path)
        self.response = ProjectsListView.as_view()(self.request)
        assert self.response.status_code == 200, 'Should be status code 200'

    def test_projects_can_be_listed_by_keywords_view(self):
        self.keywords = mixer.blend('projects.keywords')
        self.proj = mixer.blend(Project, keywords=self.keywords)
        self.path = reverse('projects:keywords_list', kwargs={'slug': self.keywords.slug})
        self.request = RequestFactory().get(self.path)
        self.response = ProjectsUsingTheseKeywordsListView.as_view()(self.request, slug=self.keywords.slug)
        assert self.response.status_code == 200, 'Should be status code 200'
