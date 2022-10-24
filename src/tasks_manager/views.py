from django.shortcuts import render

from tasks_manager.models import Task


def tasks(request):
    return render(request, "tasks_manager/tasks.html",
                  {"page_title": "Tasks - Dashboard", "tasks": Task.objects.all(), "num_tasks": Task.objects.count})
