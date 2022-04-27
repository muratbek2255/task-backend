from django.db import models

from products.models import Products
from users.models import CustomUser


class Order(models.Model):
    """Заказы"""
    customer = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    order_time = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    """Связь между заказами и продуктами"""
    products = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
