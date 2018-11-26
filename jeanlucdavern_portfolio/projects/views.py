from django.views.generic import DetailView, ListView

from .models import Project, Keywords


class ProjectsListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectsUsingTheseKeywordsListView(ListView):
    model = Project
    allow_empty = False  # If list is empty 404

    def get_queryset(self):
        return Project.objects.filter(keywords__slug=self.kwargs['slug'])


class KeywordsListView(ListView):
    model = Keywords
    allow_empty = False
