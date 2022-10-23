from datetime import datetime
from django.shortcuts import render

def homepage(request):
    return render(request, "website/homepage.html", context={"name": "John", "footer_date": datetime.today()})

def about(request):
    return render(request, "website/about.html", context={"footer_date": datetime.today()})