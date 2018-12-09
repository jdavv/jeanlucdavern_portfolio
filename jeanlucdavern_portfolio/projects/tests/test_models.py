import pytest
from django.template.defaultfilters import slugify
from mixer.backend.django import mixer


pytestmark = pytest.mark.django_db


class TestProjectsModel:
    def test_get_string_repr(self):
        proj = mixer.blend('projects.Project')
        assert str(proj) == proj.title, '__str__ should == tile'

    def test_project_title_is_slugified(self):
        proj = mixer.blend('projects.Project')
        assert proj.slug == slugify(proj.title), 'Slug should pre-populate from title'

    def test_get_absolute_url(self):
        proj = mixer.blend('projects.Project')
        assert proj.get_absolute_url() == f'/projects/{proj.slug}/', 'Should fail if urlconf is not defined correctly'


class TestKeywordsModel:
    def test_can_create_keywords_object(self):
        keyword = mixer.blend('projects.Keywords')
        assert keyword.pk == 1, 'Should create a Keywords instance'

    def test_keywords_name_gets_slugified(self):
        keyword = mixer.blend('projects.Keywords')
        assert keyword.slug == slugify(keyword.name), 'Slug should pre-populate from name'

    def test_str_is_slug(self):
        keyword = mixer.blend('projects.Keywords')
        assert str(keyword) == slugify(keyword.name), '__str__ should pre-populate from name'

    def test_get_absolute_url(self):
        keyword = mixer.blend('projects.Keywords')
        assert keyword.get_absolute_url() == f'/projects/tagged/{keyword.slug}/', 'Should fail if urlconf not defined'


class TestAboutmodel:
    def test_get_string_repr(self):
        about = mixer.blend('projects.About')
        assert str(about) == about.title, '__str__ should == title'


class TestSharingMeta:
    def test_get_string_repr(self):
        meta = mixer.blend('projects.SharingMeta')
        assert str(meta) == meta.url, '__str__ should = meta.url'
