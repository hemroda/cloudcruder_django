from datetime import date
from datetime import time

from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    code_postal = models.CharField(max_length=6)
    city = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.address1} - {self.code_postal} - {self.city}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default=time(9))
    end_date = models.TimeField(null=True, blank=True)
    duration = models.IntegerField(default=1)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
