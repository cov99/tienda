from django.shortcuts import render
from catalog.providers import product as product_providers
from catalog.providers import category as category_providers

def all_products(request):
    context = dict()
    products = product_providers.get_all_products()
    context = {
        "products": products,
    }
    return render(
        request,
        "all_products.html",
        context=context
    )

def products_by_category(request, category_id):
    context = dict()
    products = product_providers.filter_products_by_category_id(
        category_id = category_id
    )
    category = category_providers.get_category_by_id(id=category_id)
    context = {
        "products": products,
        "category": category
    }
    return render(request, "products_by_category.html", context)

