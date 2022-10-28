from django.shortcuts import render, get_object_or_404, redirect

from apps.events_manager.forms import EventForm
from apps.events_manager.models import Event


def events(request):
    return render(request, "events_manager/events.html",
                  {"page_title": "Events - Dashboard", "events": Event.objects.all(),
                   "num_events": Event.objects.count})


def event_detail(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, "events_manager/event.html", {"event": event})


def new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("events_path")
    else:
        form = EventForm()
    return render(request, "events_manager/new.html", {"form": form})
