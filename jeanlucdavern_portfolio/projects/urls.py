from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "projects"
urlpatterns = [
    path('', view=views.ProjectsListView.as_view(), name='list'),
    path('tags/', view=views.KeywordsListView.as_view(), name='keywords_list'),
    path(
        'tagged/<slug>/',
        view=views.ProjectsUsingTheseKeywordsListView.as_view(),
        name='projects_with_keywords_list'),
    path('<slug>/', view=views.ProjectDetailView.as_view(), name='detail'),
]
