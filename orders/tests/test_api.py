from django.urls import reverse
from rest_framework.test import APITestCase

from orders.models import Order
from products.models import Products


class ProductsAPITestCase(APITestCase):

    def test_order(self):
        url = reverse('orders-url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 0)

    def test_orders_with_products(self):
        new_product = Products.objects.create(title='NBA-Shirt', description='Cool', price=25000)
        order_new = Order.objects.create(customer='murat23@gmail.com', total_price='23000')
        url = reverse('orders-url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], new_product.id)
        self.assertEqual(response.data[0]['title'], new_product.title)
        self.assertEqual(response.data[0]['description'], new_product.description)
        self.assertEqual(response.data[0]['price'], new_product.price)
        self.assertEqual(response.data[0]['id'], order_new.id)
        self.assertEqual(response.data[0]['customer'], order_new.customer)
        self.assertEqual(response.data[0]['total_price'], order_new.total_price)
