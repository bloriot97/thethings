from django.db import models

from django.utils import timezone



class Announce(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    # as anyone can create an announce anonymously it is not necessary to create a user model
    author_name = models.CharField(max_length=15)
    author_email = models.EmailField(max_length=70)
    edit_date = models.DateTimeField('date published')
    private_token = models.CharField(max_length=32)
