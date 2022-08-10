from catalog.providers import category as category_providers

def default(request):
    categories = category_providers.get_all_categories()
    return dict(
       categories=categories
    )