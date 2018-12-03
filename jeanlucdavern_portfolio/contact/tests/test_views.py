from jeanlucdavern_portfolio.contact.views import ContactView
from django.urls import resolve
from django.test import RequestFactory


class TestContactView:
    # contact_page = resolve('/contact/')
    # exepcted = ContactView
    # assert contact_page.func == exepcted

    def test_contact_view(self):
        req = RequestFactory().get('/contact/')
        resp = ContactView.as_view()(req)
        assert resp.status_code == 200,  'Should be callable by anyone'
