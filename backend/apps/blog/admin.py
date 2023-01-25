from django.contrib import admin

from .models import Post
from .models import PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "intro")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(PostCategory)
admin.site.register(Post)
