from __future__ import unicode_literals

from django.db import models


class NewsPiece(models.Model):
    title = models.CharField(max_length=500, blank=True, default='')
    url = models.URLField(unique=True)


class NewsGroup(models.Model):
    name = models.CharField(max_length=200)
    news = models.ManyToManyField('NewsPiece')


