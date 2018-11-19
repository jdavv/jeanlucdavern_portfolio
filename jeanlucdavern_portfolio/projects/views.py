from django.views.generic import ListView, DetailView
from .models import Project


class ProjectsListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project
