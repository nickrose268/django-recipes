from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, FormView
from django.views.generic.detail import SingleObjectMixin

from . import forms
from . import models

# Check out following django docs for explanation of the basic idea
# https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/

class CampaignDisplayView(DetailView):

    template_name = 'campaign/campaign_detail.html'
    model = models.Campaign

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = forms.SubscriberSignupForm
        context['form'] = form
        if self.request.resolver_match.view_name == 'campaign:campaign_thanks':
            context['thanks'] = True
        return context


class CampaignSignupView(FormView, SingleObjectMixin):
    template_name = 'campaign/campaign_detail.html'
    form_class = forms.SubscriberSignupForm
    model = models.Campaign

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save(campaign=self.object)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('campaign:campaign_thanks', kwargs={'pk': self.object.pk})

class CampaignDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CampaignDisplayView.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CampaignSignupView.as_view()
        return view(request, *args, **kwargs)
