import pytest
from django.conf import settings
from django.urls import reverse, resolve


class TestUrls:

    def test_project_root(self):
        assert reverse("projects:list") == "/projects/"
        assert resolve("/projects/").view_name == "projects:list"
