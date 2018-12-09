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
        proj = mixer.blend('projects.Project')
        path = reverse('projects:detail', kwargs={'slug': proj.slug})
        request = RequestFactory().get(path)
        response = ProjectDetailView.as_view()(
            request, slug=proj.slug)
        assert response.status_code == 200, 'Should be status code 200'

    def test_project_list_view(self):
        path = reverse('projects:list')
        request = RequestFactory().get(path)
        response = ProjectsListView.as_view()(request, meta={})
        assert response.status_code == 200, 'Should be status code 200'

    def test_project_list_view_context_data(self):
        meta = mixer.blend(SharingMeta, display=True, url='/projects/')
        path = reverse('projects:list')
        request = RequestFactory().get(path)
        response = ProjectsListView.as_view()(request)
        assert response.context_data[
            'meta'].description == meta.description, 'Response context data should match meta attributes'

    def test_projects_can_be_listed_by_keywords_view(self):
        keywords = mixer.blend('projects.keywords')
        mixer.blend(Project, keywords=keywords)
        path = reverse(
            'projects:projects_with_keywords_list',
            kwargs={'slug': keywords.slug})
        request = RequestFactory().get(path)
        response = ProjectsUsingTheseKeywordsListView.as_view()(
            request, slug=keywords.slug)
        assert response.status_code == 200, 'Should be status code 200'

    def test_about_view_no_pk_and_display_is_false(self):
        mixer.blend(About, display=False)
        path = reverse('about')
        request = RequestFactory().get(path)
        with pytest.raises(Http404):
            AboutView.as_view()(request), 'Should raise 404 if no About obj exist with display= True'

    def test_about_view_no_pk_and_display_true(self):
        mixer.blend(About, display=True)
        path = reverse('about')
        request = RequestFactory().get(path)
        response = AboutView.as_view()(request)
        assert response.status_code == 200, 'Should be status code 200'

    def test_home_about_view_context_data(self):
        mixer.blend(About, display=True)
        meta = mixer.blend(SharingMeta, display=True, url='/about/')
        path = reverse('about')
        request = RequestFactory().get(path)
        response = AboutView.as_view()(request)
        assert response.context_data[
            'meta'].description == meta.description, 'Response context data should match meta attributes'

    def test_home_view_only_displays_projects_where_displayed_is_true(self):
        mixer.blend(Project, displayed_on_home_page=True)
        mixer.blend(Project, displayed_on_home_page=False)
        path = reverse('home')
        request = RequestFactory().get(path)
        response = HomeView.get_queryset(request)
        assert len(response) == 1, 'Should only display len() of Projects with displayed_on_home_page = True'

    def test_home_view_displays_base_even_if_no_projects_exists(self):
        path = reverse('home')
        request = RequestFactory().get(path)
        response = HomeView.as_view()(request)
        assert response.status_code == 200, 'Page should render even when no projects are returned in the queryset'

    def test_home_view_context_data(self):
        mixer.blend(Project, displayed_on_home_page=True)
        meta = mixer.blend(SharingMeta, display=True, url='/')
        path = reverse('home')
        request = RequestFactory().get(path)
        response = HomeView.as_view()(request)
        assert response.context_data[
            'meta'].description == meta.description, 'Response context data should match meta attributes'
