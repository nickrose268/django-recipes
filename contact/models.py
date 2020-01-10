from django.db import models

class Contact(models.Model):
    model_name = 'Contact'

    message = models.TextField()
    email = models.EmailField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    privacy_accept = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
