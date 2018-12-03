from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    path('', view=views.ContactView.as_view(), name='contact_index')
]
