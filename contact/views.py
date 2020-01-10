from django.views.generic import CreateView, TemplateView
from django.urls import reverse

from . import forms
from . import models

class ContactView(CreateView):
    form_class = forms.ContactForm
    template_name = 'contact/contact.html'
    #success_url = reverse('contact:thanks')    ## This causes a circular import error   WHY ?
    success_url = 'thanks'

class ThanksView(TemplateView):
    template_name = 'contact/thanks.html'
