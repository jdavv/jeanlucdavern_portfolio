from django.views.generic.edit import FormView
from .forms import EmailForm


class ContactView(FormView):
    template_name = 'contact/emailform.html'
    form_class = EmailForm
