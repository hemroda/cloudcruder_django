from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
