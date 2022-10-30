from django.shortcuts import render, redirect, get_object_or_404
from apps.incidents_manager.forms import TicketForm
from .models import Ticket


def index_tickets(request):
    return render(request, "incidents_manager/tickets/index.html", {"tickets": Ticket.objects.all()})


def new_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard_tickets_path")
    else:
        form = TicketForm()
    return render(request, "incidents_manager/tickets/new.html", {"form": form})


def show_ticket(request, id):
    ticket = get_object_or_404(Ticket, pk=id)
    return render(request, "incidents_manager/tickets/show.html", {"ticket": ticket})
