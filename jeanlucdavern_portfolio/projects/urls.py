from django.urls import path

from . import views

app_name = "projects"
urlpatterns = [
        path('', view=views.ProjectsListView.as_view(), name='list'),
        path('<int:pk>', view=views.ProjectDetailView.as_view(), name='detail'),
]
