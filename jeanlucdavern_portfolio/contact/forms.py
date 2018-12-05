from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Column, Layout, Submit
from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your email'}),
        required=True)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}),
        max_length=160,
        required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Column('email', 'subject', 'message'),
            HTML(
                '<div class="g-recaptcha" data-sitekey="6LdeCH8UAAAAAICyVnGPLISBlb5K6ASzSweic8Ob"></div>'
            ), Submit('send', 'Send', css_class="mt-3 mb-3"))
