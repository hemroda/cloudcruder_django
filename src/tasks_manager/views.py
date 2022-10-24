from django.shortcuts import render

from tasks_manager.models import Task


def tasks(request):
    return render(request, "tasks_manager/tasks.html", {"tasks": Task.objects.all()})
