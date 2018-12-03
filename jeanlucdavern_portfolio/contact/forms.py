from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField
    message = forms.CharField
    email = forms.EmailField
