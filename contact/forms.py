from django.core.exceptions import ValidationError
from django import forms
from . import models

class ContactForm(forms.ModelForm):
    form_name = 'Contact'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            if self.errors:
                field.widget.attrs.update({
                         'autofocus': ''
                     })
            else:
                pass

    email_repeat = forms.EmailField(max_length=200, help_text='Just to make sure we have it right...')

    class Meta():
        model = models.Contact
        fields = ('email', 'email_repeat', 'message', 'privacy_accept',)
        help_texts = {
                'privacy_accept': ('<a href="#">SEE MY PRIVACY POLICY HERE</a>'),
                'email': ('We will never share your email with anyone else!'),
                'email_repeat': ('Just to make sure we have it right...'),
        }

        widgets = {
          'message': forms.Textarea(attrs={'rows': 6}),
        }


    def clean(self):
        cd = self.cleaned_data

        email1 = cd.get("email")
        email2 = cd.get("email_repeat")

        if email1 != email2:
            raise ValidationError("Emails did not match")
            return cd

        privacy_accept = cd.get("privacy_accept")
        if privacy_accept != True:
            raise ValidationError("Please accept our privacy policy")
            return cd

        return cd

    def save(self, commit = True):
        contact = super(ContactForm, self).save(commit = False)
        # do other stuff - send email etc.
        if commit:
            contact.save()
        return contact
