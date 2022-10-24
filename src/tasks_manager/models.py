from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
