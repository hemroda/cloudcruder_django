from django.urls import path
from .views import IndexBlogView, BlogDetailView

urlpatterns = [
    path("", IndexBlogView.as_view(), name="blog_index_path"),
    path("/<int:pk>/", BlogDetailView.as_view(), name="blog_detail_path")
]
