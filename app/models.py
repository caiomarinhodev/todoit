import datetime

from django.db import models


# Create your models here.

class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(Timestamp):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)

    def __str__(self):
        return self.title
