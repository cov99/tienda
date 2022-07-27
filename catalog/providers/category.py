from catalog.models import Category

def get_all_categories():
    categories = Category.objects.all()
    return categories 

def filter_categories_by_name(name:str):
    categories = Category.objects.filter(name__icontains=name)
    return categories
