import pytest
from django.http.response import Http404
from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer

from jeanlucdavern_portfolio.projects.views import (
    AboutView, HomeView, ProjectDetailView, ProjectsListView,
    ProjectsUsingTheseKeywordsListView)

from ..models import About, Project, SharingMeta


@pytest.mark.django_db
class TestProjectViews:
    def test_project_detail_view(self):
        self.proj = mixer.blend('projects.Project')
        self.path = reverse('projects:detail', kwargs={'slug': self.proj.slug})
        self.request = RequestFactory().get(self.path)
        self.response = ProjectDetailView.as_view()(
            self.request, slug=self.proj.slug)
        assert self.response.status_code == 200, 'Should be status code 200'

    def test_project_list_view(self):
        self.path = reverse('projects:list')
        self.request = RequestFactory().get(self.path)
        self.response = ProjectsListView.as_view()(self.request, meta={})
        assert self.response.status_code == 200, 'Should be status code 200'

    def test_project_list_view_context_data(self):
        self.proj = mixer.blend(Project)
        self.meta = mixer.blend(SharingMeta, display=True, url='/projects/')
        self.path = reverse('projects:list')
        self.request = RequestFactory().get(self.path)
        self.response = ProjectsListView.as_view()(self.request)
        assert self.response.context_data[
            'meta'].description == self.meta.description

    def test_projects_can_be_listed_by_keywords_view(self):
        self.keywords = mixer.blend('projects.keywords')
        self.proj = mixer.blend(Project, keywords=self.keywords)
        self.path = reverse(
            'projects:projects_with_keywords_list',
            kwargs={'slug': self.keywords.slug})
        self.request = RequestFactory().get(self.path)
        self.response = ProjectsUsingTheseKeywordsListView.as_view()(
            self.request, slug=self.keywords.slug)
        assert self.response.status_code == 200, 'Should be status code 200'

    def test_about_view_no_pk_and_display_is_false(self):
        self.about = mixer.blend(About, display=False)
        self.path = reverse('about')
        self.request = RequestFactory().get(self.path)
        with pytest.raises(Http404):
            self.response = AboutView.as_view()(self.request)

    def test_about_view_no_pk_and_display_true(self):
        self.about = mixer.blend(About, display=True)
        self.path = reverse('about')
        self.request = RequestFactory().get(self.path)
        self.response = AboutView.as_view()(self.request)
        assert self.response.status_code == 200

    def test_home_about_view_context_data(self):
        self.about = mixer.blend(About, display=True)
        self.meta = mixer.blend(SharingMeta, display=True, url='/about/')
        self.path = reverse('about')
        self.request = RequestFactory().get(self.path)
        self.response = AboutView.as_view()(self.request)
        assert self.response.context_data[
            'meta'].description == self.meta.description

    def test_home_view_only_displays_projects_where_displayed_is_true(self):
        self.proj1 = mixer.blend(Project, displayed_on_home_page=True)
        self.proj2 = mixer.blend(Project, displayed_on_home_page=False)
        self.path = reverse('home')
        self.request = RequestFactory().get(self.path)
        self.response = HomeView.get_queryset(self.request)
        assert len(self.response) == 1

    def test_home_view_where_all_projects_displayed_false(self):
        self.proj1 = mixer.blend(Project, displayed_on_home_page=False)
        self.path = reverse('home')
        self.request = RequestFactory().get(self.path)
        self.response = HomeView.as_view()(self.request)
        assert self.response.status_code == 200, 'Page should render even when no projects are returned in the queryset'

    def test_home_view_context_data(self):
        self.proj = mixer.blend(Project, displayed_on_home_page=True)
        self.meta = mixer.blend(SharingMeta, display=True, url='/')
        self.path = reverse('home')
        self.request = RequestFactory().get(self.path)
        self.response = HomeView.as_view()(self.request)
        assert self.response.context_data[
            'meta'].description == self.meta.description
