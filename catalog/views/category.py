from django.shortcuts import render
from catalog.providers import category as category_providers

def all_categories(request):
    context = dict()
    categories = category_providers.get_all_categories()
    context["categories"] = categories

    return render(
        request,
        "all_categories.html",
        context = context
    )