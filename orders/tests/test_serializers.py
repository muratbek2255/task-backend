import io

from django.core.files.images import ImageFile
from django.test import TestCase

from orders.models import Order, OrderItem
from products.models import Products
from products.serializers import OrderSerializer
from users.models import CustomUser


class ProductSerializerTestCase(TestCase):
    def test_product_category_with_product_serializer(self):
        order = Order.objects.create(customer=CustomUser, total_price=20000 )
        phone = Products.objects.create(title='SI MuCho', image=ImageFile(io.BytesIO(b'some-file'), name='test-image4.jpg'), price=20000,
                                       description='new', category=order)

        srz = OrderSerializer(order, many=False)
        expected_data = {
            'products': [
                {
                    'id': phone.id,
                    'title': phone.title,
                    'image': phone.image,
                    'description': phone.description,
                    'price': phone.price,
                    'category_name': order.title,
                }
            ],
            'order': [
                {
                    'id': order.id,
                    'customer': order.customer,
                    'total_price': order.total_price,
                }
            ],
        }
        result = srz.data
        self.assertEqual(result, expected_data)
