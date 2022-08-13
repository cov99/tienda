from orders.models import CartProduct

def add_product_to_cart(product, cart, quantity):
    cart_product = CartProduct.objects.create(
        product = product,
        cart = cart, 
        quantity = quantity
    ) 
    return cart_product

def get_products_by_cart_id(cart_id):
    products = CartProduct.objects.filter(cart__id = cart_id)
    return products

def remove_product_from_cart_by_id(cart_product_id):
    cart_product = CartProduct.objects.get(id=cart_product_id)
    cart_product.delete()
    

