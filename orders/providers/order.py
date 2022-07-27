from orders.models import Order

def get_orders_from_user_id(user_id:int):
    orders = Order.objects.filter(user__id=user_id)
    return orders

def get_order_by_id(order_id:int):
    order = Order.objects.get(id=order_id)
    return order

def create_order(
    comments:str,
    address:str,
    commune:str,
    net_amount:int,
    iva_amount:int,
    total_amount:int,
    user_id:int
):
    order = Order.objects.create(
        comments=comments,
        address=address,
        commune=commune,
        net_amount=net_amount,
        iva_amount=iva_amount,
        total_amount=total_amount,
        user=user_id
    )
    return order 
    