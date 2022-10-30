from django.shortcuts import render, get_object_or_404
from .models import Product


def index_products(request):
    return render(request, "store/products/index.html", {"products": Product.objects.all()})


def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "store/products/show.html", {"product": product})
