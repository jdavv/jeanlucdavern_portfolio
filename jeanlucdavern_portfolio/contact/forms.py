from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column


class EmailForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=160, required=True)
    message = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column('email', 'subject', 'message'), Submit('send', 'send'))
