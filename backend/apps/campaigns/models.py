from django.db import models


class Campaign(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
