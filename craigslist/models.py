from django.db import models

from django.utils import timezone

from django.shortcuts import reverse


# I should have implemented ModelForm


class Announce(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    # as anyone can create an announce anonymously it is not necessary to create a user model
    author_name = models.CharField(max_length=15)
    author_email = models.EmailField(max_length=70)
    edit_date = models.DateTimeField('date published')
    private_token = models.CharField(max_length=32)

    def getEditUri(self):
        return "/" + str(self.pk) + '/edit/?key=' + self.private_token


    def __str__(self):
        return self.title + "[" + author_name + "]:" + self.description

class Mail(models.Model):
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    author_name = models.CharField(max_length=15)
    author_email = models.EmailField(max_length=70)
    body = models.CharField(max_length=500)
