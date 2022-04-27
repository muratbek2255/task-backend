from django.test import TestCase
from django.contrib.auth import get_user_model

from products.serializers import UserSerializer

User = get_user_model()


class CustomUserTestCase(TestCase):
    def test_user_serializer(self):
        user = User.objects.create(email='test12@gmail.com', password='12345678',
                                   password2='12345678')
        srz = UserSerializer(user, many=False)
        expected_data = {
            'id': user.id,
            'email': user.email,
            'password': user.password,
            'password2': user.password2
        }
        self.assertEqual(srz.data, expected_data)


