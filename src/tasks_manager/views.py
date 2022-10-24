from django.forms import modelform_factory
from django.shortcuts import render, redirect

from tasks_manager.models import Task


def tasks(request):
    return render(request, "tasks_manager/tasks.html",
                  {"page_title": "Tasks - Dashboard", "tasks": Task.objects.all(), "num_tasks": Task.objects.count})


TaskForm = modelform_factory(Task, exclude=["start_date", "finish_date"])


def new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks_path")
    else:
        form = TaskForm()
    return render(request, "tasks_manager/new.html", {"form": form})
