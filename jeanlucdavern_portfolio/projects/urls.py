from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
        path('', view=views.ProjectsListView.as_view(), name='list'),
        path('<slug>', view=views.ProjectDetailView.as_view(), name='detail'),
        path('tagged/<slug>', view=views.TechnologiesListView.as_view(), name='tech_list'),
]
