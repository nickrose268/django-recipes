from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('campaign.urls', namespace='campaign')),
    path('admin/', admin.site.urls),
]
