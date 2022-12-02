from django.views.generic import ListView, DetailView

from .models import Post


class IndexBlogView(ListView):
    model = Post
    template_name = "blog/index.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
