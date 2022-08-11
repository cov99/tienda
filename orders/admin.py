from django.contrib import admin
from orders.models import Order, OrderProduct, Cart, CartProduct

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass 

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    pass 

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass 

@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass 
