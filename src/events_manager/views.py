from django.shortcuts import render, get_object_or_404

from events_manager.models import Event


def events(request):
    return render(request, "events_manager/events.html", {"events": Event.objects.all(), "num_events": Event.objects.count})


def event_detail(request, id):
    event = get_object_or_404(Event, pk=id)
    return render(request, "events_manager/event.html", {"event": event})
