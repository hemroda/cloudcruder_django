from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("blog_detail_path", kwargs={"pk": self.pk})
