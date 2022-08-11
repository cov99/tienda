from catalog.providers import category as category_providers
from orders.providers import cart as cart_providers
from orders.providers import cart_product as cart_product_providers

def default(request):
   context = dict()
   context["categories"] = category_providers.get_all_categories()
   if request.user.is_authenticated:
      user_id = request.user.id
      cart = cart_providers.get_cart_by_user_id(user_id=user_id)
      cart_products = cart_product_providers.get_products_by_cart_id(cart_id=cart.id)
      context["cart_products"] = cart_products
      context["cart_total"] = cart_providers.get_cart_total_price_by_id(cart_id=cart.id)
      

   return context 



