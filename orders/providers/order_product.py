from orders.models import OrderProduct

def get_order_products_by_order_id(order_id:int):
    order_products = OrderProduct.objects.filter(order__id=order_id)
    return order_products

def create_order_product(
    quantity,
    product,
    order
):
    total = product.price*quantity
    order_product = OrderProduct.objects.create(
        quantity=quantity,
        total_amount=total,
        product=product,
        order=order
    )
    return order_product
    