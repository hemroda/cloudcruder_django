from django.urls import path

from . import views


urlpatterns = [
    path("", views.tasks, name="tasks_path"),
    path("new", views.new, name="new_task_path")
]