from django.db import models

class Campaign(models.Model):

    title = models.CharField('Title', max_length=250, unique=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):

    name = models.CharField('Your Name', max_length=100, blank=True, null=True)
    email = models.EmailField('Your Email', max_length=100)
    campaign = models.ManyToManyField(Campaign, 'subscriber')

    def __str__(self):
        return self.email
