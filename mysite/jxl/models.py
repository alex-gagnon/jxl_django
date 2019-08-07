import datetime

from django.db import models
# Create your models here.
from django.forms import ModelForm
from django.utils import timezone


class JXLModel(models.Model):
    project_code = models.CharField(max_length=50, default='default')
    project_text = models.CharField(max_length=100, default='default')

    filter_by_text = models.CharField(max_length=100, default='default')

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

