from jeanlucdavern_portfolio.contact.views import ContactView, SuccessView
from django.test import RequestFactory
from django.test import Client
import pytest


@pytest.mark.django_db
class TestContactView:
    def test_contact_view(self):
        req = RequestFactory().get('/contact/')
        resp = ContactView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_contact_success_view(self):
        req = RequestFactory().get('/contact/success/')
        resp = SuccessView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_contact_view_redirects_with_valid_form_submitted(self):
        client = Client()
        resp = client.post(
            '/contact/', {
                'email': 'valid@email.com',
                'subject': 'a valid subject',
                'message': 'a valid message'
            })
        assert resp.status_code == 302
