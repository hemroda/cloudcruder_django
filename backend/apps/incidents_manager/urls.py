from django.urls import path

from . import views


urlpatterns = [
    path("", views.index_tickets, name="dashboard_tickets_path"),
    path("new", views.new_ticket, name="new_dashboard_ticket_path"),
    path("<int:id>", views.show_ticket, name="dashboard_ticket_path")
]
