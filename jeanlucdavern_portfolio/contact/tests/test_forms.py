from jeanlucdavern_portfolio.contact.forms import EmailForm


class TestForms:
    def test_emailform(self):
        form = EmailForm({
            'email': 'valid@email.com',
            'subject': 'valid subject',
            'message': 'valid message'
        })

        assert form.is_valid() is True
