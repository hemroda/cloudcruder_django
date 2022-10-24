from django.urls import path

from . import views


urlpatterns = [
    path("", views.events, name="events_path"),
    path("<int:id>", views.event_detail, name="event_detail_path"),
    path("new", views.new, name="new_event_path")
]
