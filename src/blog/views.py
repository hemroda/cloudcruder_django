from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")

def article(request, article_id):
    return render(request, "blog/article.html")

