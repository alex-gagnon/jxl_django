# Create your models here.

import datetime

from django.db import models
from django.utils import timezone


class Project(models.Model):
    project_code = models.CharField(max_length=50, default='')
    project_text = models.CharField(max_length=100, default='')

    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.project_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Filter(models.Model):
    project_text = models.ForeignKey(Project, on_delete=models.CASCADE)

    filter_by_code = models.CharField(max_length=50, default='')
    filter_by_text = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.filter_by_text
