from orders.models import Cart
from orders.providers import cart_product as cart_products_providers

def get_or_create_cart(user):
    try:
        cart = Cart.objects.get(user=user)
        return cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)
        return cart


def get_cart_by_user_id(user_id):
    try:
        cart = Cart.objects.get(user__id=user_id)
        return cart
    except Cart.DoesNotExist:
        return None

def get_cart_total_price_by_id(cart_id):
    cart_products = cart_products_providers.get_products_by_cart_id(cart_id=cart_id)
    total = 0

    for cart_product in cart_products:
        total += cart_product.product.price * cart_product.quantity
   
    return total
