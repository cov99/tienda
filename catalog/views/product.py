from django.shortcuts import render
from catalog.providers import product as product_providers

def all_products(request):
    context = dict()
    products = product_providers.get_all_products()
    context["products"] = products
    return render(
        request,
        "all_products.html",
        context=context
    )