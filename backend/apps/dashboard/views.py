from datetime import datetime

from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard/dashboard.html",
                  context={"page_title": "Dashboard - Maavita", "name": "First Account",
                           "footer_date": datetime.today()})
