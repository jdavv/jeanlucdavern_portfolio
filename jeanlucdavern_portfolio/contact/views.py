from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import EmailForm


class ContactView(FormView):
    template_name = 'contact/emailform.html'
    form_class = EmailForm
    success_url = 'success/'


class SuccessView(TemplateView):
    template_name = 'contact/emailsuccess.html'
