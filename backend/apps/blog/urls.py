from django.urls import path
from .views import IndexBlogView, BlogDetailView

urlpatterns = [
    path("blog", IndexBlogView.as_view(), name="blog_index_path"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail_path")
]
