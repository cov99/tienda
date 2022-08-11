from http.client import HTTPResponse
from django.shortcuts import render, redirect 
from orders.providers import cart as cart_providers
from catalog.providers import product as product_providers
from orders.providers import cart_product as cart_product_providers
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse


def add_product_to_cart(request):
    if request.method == "POST" and request.user.is_authenticated:
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        user_id = request.user.id
        cart = cart_providers.get_cart_by_user_id(user_id=user_id)
        product = product_providers.get_product_by_id(product_id=product_id)
        cart_product_providers.add_product_to_cart(
            product = product,
            cart = cart,
            quantity = quantity
        )
        messages.success(request, "El producto se agrego correctamente")
        return redirect(reverse("index"))
    else:
        messages.warning(
            request, 
            "Debes iniciar sesion para añadir productos a tu carrito"
        )
        return redirect(reverse("index"))

