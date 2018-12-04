from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .forms import EmailForm
import os

RECIPIENT_LIST = os.environ['DJANGO_MAILTO']


class ContactView(FormView):
    template_name = 'contact/emailform.html'
    form_class = EmailForm
    success_url = 'success/'

    def form_valid(self, form):
        from_email = self.request.POST.get('email')
        subject = self.request.POST.get('subject')
        message = self.request.POST.get('message')
        send_mail(subject, message, from_email, [RECIPIENT_LIST], fail_silently=True)
        return super(ContactView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = 'contact/emailsuccess.html'
