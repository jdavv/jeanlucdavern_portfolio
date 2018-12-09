from django.views.generic import DetailView, ListView, TemplateView

from django.shortcuts import get_object_or_404, resolve_url

from django.http import Http404

from .models import Project, Keywords, About, SharingMeta

from meta.views import MetadataMixin

from django.core.exceptions import ObjectDoesNotExist


class HomeView(MetadataMixin, ListView):
    model = Project

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

    # def get_context_data(self, **kwargs):
        # context = super(HomeView, self).get_context_data(**kwargs)
        # context['meta'] = get_object_or_404(
            # SharingMeta, display=True, url=resolve_url('/')).as_meta(self.request)
        # return context


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

    # def get_context_data(self, **kwargs):
        # context = super(AboutView, self).get_context_data(**kwargs)
        # context['meta'] = get_object_or_404(
            # SharingMeta, display=True,
            # url=resolve_url('about')).as_meta(self.request)
        # return context


class ProjectsListView(MetadataMixin, ListView):
    model = Project

    # def get_context_data(self, **kwargs):
    # context = super(ProjectsListView, self).get_context_data(**kwargs)
    # context['meta'] = get_object_or_404(
    # SharingMeta, display=True,
    # url=resolve_url('/projects/')).as_meta(self.request)
    # return context
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


class ProjectsUsingTheseKeywordsListView(ListView):
    model = Project
    allow_empty = False  # If list is empty 404

    def get_queryset(self):
        return Project.objects.filter(keywords__slug=self.kwargs['slug'])


class KeywordsListView(ListView):
    model = Keywords
    allow_empty = False

    # html meta tags
    description = 'Find projects that have been tagged with a specific technology'
    title = 'Projects tagged by keyword'
    twitter_card = 'summary'
    use_facebook = 'True'
    object_type = 'website'
