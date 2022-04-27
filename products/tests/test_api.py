from django.urls import reverse
from rest_framework.test import APITestCase

from products.models import Products


class ProductsAPITestCase(APITestCase):

    def test_products_view_with_no_exists_products(self):
        url = reverse('products-url')  # url = "/api/v1/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 0)

    def test_products_view_with_product(self):
        new_product = Products.objects.create(title='Телефон', description='Надёжный и китайский', price=25000)
        url = reverse('products-url')  # url = "/api/v1/products/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], new_product.id)
        self.assertEqual(response.data[0]['title'], new_product.title)
        self.assertEqual(response.data[0]['description'], new_product.description)
        self.assertEqual(response.data[0]['price'], new_product.price)