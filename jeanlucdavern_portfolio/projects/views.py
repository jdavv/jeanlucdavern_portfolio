from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Project, Technologies


class ProjectsListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class TechnologiesListView(ListView):
    model = Technologies

    def get_queryset(self):
        return Technologies.objects.filter(slug=self.request.GET.get('slug'))
