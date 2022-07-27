from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass 