from django.views.generic import DetailView, ListView

from .models import Project


class ProjectsListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectsUsingTheseTechnologiesListView(ListView):
    model = Project
    allow_empty = False  # If list is empty 404

    def get_queryset(self):
        return Project.objects.filter(technologies__slug=self.kwargs['slug'])
