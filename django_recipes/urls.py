from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('campaign.urls', namespace='campaign')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('admin/', admin.site.urls),
]
