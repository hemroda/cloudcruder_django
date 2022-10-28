from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_routes, name="api_dashboard_notes_routes_path"),
    path("all", views.notes, name="api_dashboard_notes_path"),
    path("<str:pk>", views.note, name="api_dashboard_note_path")
]
