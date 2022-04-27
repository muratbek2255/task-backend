from django.contrib import admin

from orders.models import Order, OrderItem
from products.models import Category, Products
from users.models import CustomUser


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass
