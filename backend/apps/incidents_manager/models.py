from django.db import models


class Ticket(models.Model):
    submitter = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
