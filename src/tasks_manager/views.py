from django.shortcuts import render


def tasks(request):
    return render(request, "tasks_manager/tasks.html")


def task(request):
    return render(request, "tasks_manager/task.html")
