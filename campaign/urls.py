from django.urls import path
from . import views

app_name = 'campaign'

urlpatterns = [
    path('campaign/<int:pk>', views.CampaignDetailView.as_view(), name='campaign_detail'),
    path('campaignthanks/<int:pk>', views.CampaignDetailView.as_view(), name='campaign_thanks'),
    path('campaignsignup/<int:pk>', views.CampaignSignupView.as_view(), name='campaign_signup'),
]
