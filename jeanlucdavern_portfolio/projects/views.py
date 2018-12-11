from django.views.generic import DetailView, ListView, TemplateView

from django.shortcuts import get_object_or_404, resolve_url

from django.http import Http404

from .models import Project, Keywords, About, SharingMeta

from meta.views import MetadataMixin

from django.core.exceptions import ObjectDoesNotExist


class HomeView(MetadataMixin, ListView):
    model = Project
    template_name = 'projects/home_list.html'

    def get_queryset(self):
        return Project.objects.filter(displayed_on_home_page=True)

    def get_context_data(self, **kwargs):
        try:
            context = super(HomeView, self).get_context_data(**kwargs)
            context['meta'] = SharingMeta.objects.get(display=True, url=resolve_url('/')).as_meta(self.request)
            return context
        except ObjectDoesNotExist:
            context = super(HomeView, self).get_context_data(**kwargs)
            return context


class AboutView(DetailView):
    model = About

    def get_object(self):
        try:
            about = About.objects.get(display=True)
        except ObjectDoesNotExist:
            raise Http404('No About Stories Found')
        return about

    def get_context_data(self, **kwargs):
        try:
            context = super(AboutView, self).get_context_data(**kwargs)
            context['meta'] = SharingMeta.objects.get(display=True, url=resolve_url('/about/')).as_meta(self.request)
            return context
        except ObjectDoesNotExist:
            context = super(AboutView, self).get_context_data(**kwargs)
            return context


class ProjectsListView(MetadataMixin, ListView):
    model = Project

    def get_context_data(self, **kwargs):
        try:
            context = super(ProjectsListView, self).get_context_data(**kwargs)
            context['meta'] = SharingMeta.objects.get(display=True, url=resolve_url('/projects/')).as_meta(self.request)
            return context
        except ObjectDoesNotExist:
            context = super(ProjectsListView, self).get_context_data(**kwargs)
            return context


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)

        context['meta'] = self.get_object().as_meta(self.request)
        return context


class ProjectsUsingTheseKeywordsListView(MetadataMixin, ListView):
    model = Project
    allow_empty = False  # If list is empty 404

    def get_queryset(self):
        return Project.objects.filter(keywords__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProjectsUsingTheseKeywordsListView, self).get_context_data(**kwargs)

        context['meta'] = Keywords.objects.get(slug=self.kwargs['slug']).as_meta(self.request)
        return context


class KeywordsListView(ListView):
    model = Keywords
    allow_empty = False
