from django.views.generic import DetailView, ListView, TemplateView

from .models import Project, Keywords

from meta.views import MetadataMixin


class HomeView(MetadataMixin, TemplateView):
    description = 'jdavs baddazz site'
    template_name = 'pages/home.html'
    use_twitter = 'True'
    twitter_card = 'player'
    image = 'https://media.giphy.com/media/onozNDEOoj3nW/giphy.gif'
    title = 'I type a lot'
    extra_props = {
        'twitter:player:width': '320',
        'twitter:player:height': '180',
        'twitter:player:stream': 'https://media.giphy.com/media/onozNDEOoj3nW/giphy.gif'
    }


class ProjectsListView(MetadataMixin, ListView):
    model = Project
    description = (
        'A list of my projects. A mix of Python, Linux, django,' +
        'QEMU/KVM, and AWS. Making life easy by building systems that do cool things.'
    )
    use_twitter = 'True'
    title = 'Check out a list software and systems I designed'
    image = '/images/monkeycomputer.gif'
    twitter_card = 'summary'


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
