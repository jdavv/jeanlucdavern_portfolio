from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=160, required=True)
    message = forms.CharField(required=True)
