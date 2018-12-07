from django.views.generic import DetailView, ListView, TemplateView

from .models import Project, Keywords

from meta.views import MetadataMixin


class HomeView(MetadataMixin, TemplateView):
    template_name = 'pages/home.html'

    # html meta tags
    title = 'Jean-Luc Davern'
    description = 'Devloper, administrator, trouble-shooter, and problem solver.'
    use_twitter = 'True'
    twitter_card = 'summary'
    object_type = 'website'


class AboutView(MetadataMixin, TemplateView):
    template_name = 'pages/about.html'

    # html meta tags
    title = 'Jean-Luc Davern'
    description = 'Devloper, administrator, trouble-shooter, and problem solver.'
    use_twitter = 'True'
    twitter_card = 'summary'
    object_type = 'website'


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
