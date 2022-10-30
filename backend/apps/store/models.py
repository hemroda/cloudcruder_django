from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    price = models.FloatField(default=0.00)
    weight = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
