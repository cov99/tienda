from catalog.models import Product
#obtener todos los productos
#filtrar productos por cateforia id
#filtrar productos por nombre

def get_all_products():
    products = Product.objects.all()
    return products

def filter_products_by_category_id(category_id:str):
    products = Product.objects.filter(category__id=category_id)
    return products

def filter_products_by_name(name:str):
    products = Product.objects.filter(name__icontains=name)
    return products 
    



