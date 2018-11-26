from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
    path('', view=views.ProjectsListView.as_view(), name='list'),
    path('tagged/', view=views.KeywordsListView.as_view(), name='keywords_list'),
    path(
        'tagged/<slug>/',
        view=views.ProjectsUsingTheseKeywordsListView.as_view(),
        name='projects_with_keywords_list'),
    path('<slug>/', view=views.ProjectDetailView.as_view(), name='detail'),
]
