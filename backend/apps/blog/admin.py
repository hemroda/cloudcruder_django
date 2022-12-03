from django.contrib import admin

from .models import Post
from .models import PostCategory

admin.site.register(PostCategory)
admin.site.register(Post)
