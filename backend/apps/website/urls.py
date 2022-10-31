from django.urls import path
from .views import HomepageView, AboutView

urlpatterns = [
    path("", HomepageView.as_view(), name="website_homepage_path"),
    path("about", AboutView.as_view(), name="website_about_path")
]
