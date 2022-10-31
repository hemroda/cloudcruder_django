from datetime import datetime
from django.shortcuts import render
from django.views import View


FOOTER_DATE = datetime.today()


class HomepageView(View):
    template_name = "website/homepage.html"

    def get(self, request):
        return render(request, self.template_name, {"page_title": "Maavita", "footer_date": FOOTER_DATE})


class AboutView(View):
    template_name = "website/about.html"

    def get(self, request):
        return render(request, self.template_name, {"page_title": "About - Maavita", "footer_date": FOOTER_DATE})
