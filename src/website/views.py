from datetime import datetime
from django.shortcuts import render


def homepage(request):
    return render(request, "website/homepage.html",
                  context={"page_title": "Maavita", "name": "John", "footer_date": datetime.today()})


def about(request):
    return render(request, "website/about.html", context={
        "page_title": "About - Maavita", "footer_date": datetime.today()
    })
