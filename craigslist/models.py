from django.db import models
from django.forms import ModelForm
from django.utils import timezone

from django.shortcuts import reverse

import string
import random


def genKey():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))


class Announce(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    # as anyone can create an announce anonymously it is not necessary to create a user model
    author_name = models.CharField(max_length=15)
    author_email = models.EmailField(max_length=70)
    edit_date = models.DateTimeField('date published', default=timezone.now)
    private_token = models.CharField(max_length=32, default=genKey)

    def getEditUri(self):
        return "/" + str(self.pk) + '/edit/?key=' + self.private_token


    def __str__(self):
        return self.title + "[" + self.author_name + "]:" + self.description

class Mail(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    date = models.DateTimeField('date published', default=timezone.now)
    author_name = models.CharField(max_length=15)
    author_email = models.EmailField(max_length=70)
    body = models.CharField(max_length=500)

class AnnounceForm(ModelForm):
    class Meta:
        model = Announce
        exclude = ['edit_date', 'private_token']

class MailForm(ModelForm):
    class Meta:
        model = Mail
        exclude = ['date']
        #fields = '__all__'
