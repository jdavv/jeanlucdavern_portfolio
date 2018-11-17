import pytest
from django.conf import settings
from django.urls import reverse, resolve


def test_list():
    assert reverse("projects:index") == "/projects/"
    assert resolve("/projects/").view_name == "projects:index"
