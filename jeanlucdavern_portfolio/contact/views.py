import os

import requests
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import EmailForm

RECIPIENT_LIST = os.environ['DJANGO_MAILTO']
RECAPTCHA_SECRET_KEY = os.environ['RECAPTCHA_SECRET_KEY']


class ContactView(FormView):
    template_name = 'contact/emailform.html'
    form_class = EmailForm
    success_url = 'success/'

    def form_valid(self, form):
        from_email = self.request.POST.get('email')
        subject = self.request.POST.get('subject')
        message = self.request.POST.get('message')

        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response,
        }

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)

        recaptcha_result = recaptcha_request.json()
        if recaptcha_result['success']:
            send_mail(
                subject,
                message,
                from_email, [RECIPIENT_LIST],
                fail_silently=True)
            return super(ContactView, self).form_valid(form)
        else:
            return redirect('/contact/')


class SuccessView(TemplateView):
    template_name = 'contact/emailsuccess.html'
