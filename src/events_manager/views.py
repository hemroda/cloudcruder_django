from django.shortcuts import render


def events(request):
    return render(request, "events_manager/events.html")


def event(request):
    return render(request, "events_manager/event.html")
