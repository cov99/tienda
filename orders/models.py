from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        app_label = "orders"

    def __str__(self):
        return str(self.user)

class CartProduct(models.Model):
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        app_label = "orders"

    def __str__(self):
        return str(self.product)

class Order(models.Model):
    comments = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    net_amount = models.PositiveIntegerField(default=0)
    iva_amount = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        app_label = "orders"

    def __str__(self):
        return f"{str(self.user)} -- {self.created_at}"

class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    total_amount = models.PositiveIntegerField(default=0)
    product = models.ForeignKey("catalog.Product", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        app_label = "orders"

    def __str__(self):
        return f"{str(self.product)} -- {self.quantity}"
        


