from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list_url"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog_detail_path"),
]
