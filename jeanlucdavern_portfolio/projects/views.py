from django.views.generic import DetailView, ListView, TemplateView

from django.shortcuts import get_object_or_404

from .models import Project, Keywords, About

from meta.views import MetadataMixin


class HomeView(MetadataMixin, ListView):
    model = Project

    # html meta tags
    title = 'Jean-Luc Davern'
    description = 'Devloper, administrator, trouble-shooter, and problem solver.'
    use_twitter = 'True'
    twitter_card = 'summary'
    object_type = 'website'
    image = 'https://s3.amazonaws.com/portfoliostatic1/media/monkeycomputer.gif'

    def get_queryset(self):
        return Project.objects.filter(displayed_on_home_page=True)


class AboutView(DetailView):
    model = About

    def get_object(self):
        if 'pk' not in self.kwargs:
            return get_object_or_404(About, displayed_on_about_page=True)

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        context['meta'] = self.get_object().as_meta(self.request)
        return context


class ProjectsListView(MetadataMixin, ListView):
    model = Project

    # html meta tags
    title = 'Software and systems I designed'
    description = (
        'Mix of Python, Linux, django,' +
        'QEMU/KVM, and AWS. Making life easy by building systems that do cool things.'
    )
    use_twitter = 'True'
    twitter_card = 'summary'
    object_type = 'website'


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
