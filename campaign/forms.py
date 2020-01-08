from django.core.exceptions import ValidationError
from django import forms
from . import models

#This is not actually used in this example
class CampaignForm(forms.ModelForm):
    class Meta():
        model = models.Campaign
        fields = ('title',)

class SubscriberSignupForm(forms.ModelForm):
    form_name = 'Subscriber Signup'
    class Meta():
        model = models.Subscriber
        fields = ('name', 'email',)

    def save(self, commit=True, **kwargs):
        m = super().save(commit=True)
        set_list=[kwargs['campaign'],]
        m.campaign.set(set_list)
        # Do anything else such as sending a confirmation email....
        return m
