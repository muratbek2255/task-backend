from django.urls import reverse
from rest_framework.test import APITestCase

from users.models import CustomUser


class ProductsAPITestCase(APITestCase):

    def test_users(self):
        url = reverse('products-url')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 203)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 0)