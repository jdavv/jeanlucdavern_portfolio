from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Column


class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}), max_length=160, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Column('email', 'subject', 'message'), Submit('send', 'Send'))

        def form_valid(self, form):
            print(self.form.cleaned_data['email'])
            print(self.request.POST.get['subject'])
            return super(EmailForm, self).form_valid(form)
