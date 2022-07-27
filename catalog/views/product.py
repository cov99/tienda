from django.shortcuts import render
from catalog.providers import product as product_providers
from catalog.providers import category as category_providers

def all_products(request):
    context = dict()
    products = product_providers.get_all_products()
    categories = category_providers.get_all_categories()
    context = {
        "products": products,
        "categories": categories
    }
    return render(
        request,
        "all_products.html",
        context=context
    )