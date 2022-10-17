from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request, "maavita/index.html", context={"name": "John", "footer_date": datetime.today()})

