from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_products, name="store_products_path"),
    path("<int:id>", views.show_product, name="store_product_path")
]
