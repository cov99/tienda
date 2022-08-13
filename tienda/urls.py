"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from catalog.views.product import all_products, products_by_category
from catalog.views.category import all_categories
from orders.views import add_product_to_cart, checkout, remove_product_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_products, name='index'),
    path('/all-categories/', all_categories, name='all_categories'),
    path('/add-product/', add_product_to_cart, name='add_product_to_cart'),
    path('products-category/<category_id>/', products_by_category, name='products_by_category'),
    path("checkout/", checkout, name="checkout"),
    path("remove-product/", remove_product_from_cart, name="remove_product"),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)