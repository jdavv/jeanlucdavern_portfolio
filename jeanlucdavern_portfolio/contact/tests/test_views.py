from jeanlucdavern_portfolio.contact.views import ContactView
from django.urls import resolve


class ContactViewTest:
    contact_page = resolve('contact/')
    exepcted = ContactView
    assert contact_page.func == exepcted
