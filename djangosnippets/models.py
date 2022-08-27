from django.db import models
from django.utils import timezone

import datetime
from django.contrib import admin

# Create your models here.
class All_snippets (models.Model):
    Title_text = models.FileField(upload_to='photos/%Y/%m/%d')
    Tags_text = models.CharField(max_length=200)
    Author_text = models.CharField(max_length=200)
    Publication_date = models.DateTimeField('date published')
    Rating_text = models.PositiveSmallIntegerField()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.Publication_date <= now
    
    def __str__(self):
        return self.Publication_date
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    
