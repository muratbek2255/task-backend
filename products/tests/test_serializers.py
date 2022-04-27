import io

from django.core.files.images import ImageFile
from django.test import TestCase

from products.models import Products, Category
from products.serializers import ProductSerializer, ProductCategorySerializer


class ProductSerializerTestCase(TestCase):

    def test_product_serializer(self):
        product = Products.objects.create(title='Man United T-Shirt', image=ImageFile(io.BytesIO(b'some-file'), name='test-image.jpg'),
                                          description='wow', price=20000)
        srz = ProductSerializer(product, many=False)
        expected_data = {
            'id': product.id,
            'title': 'Man United T-Shirt',
            'image': ImageFile(io.BytesIO(b'some-file'), name='test-image.jpg'),
            'description': 'wow',
            'price': 20000,
        }
        self.assertEqual(srz.data, expected_data)

    def test_product_serializer_many(self):
        Products.objects.create(title='Man United T-Shirt2',image=ImageFile(io.BytesIO(b'some-file'), name='test-image2.jpg'), description='ll', price=20005)
        Products.objects.create(title='Man United T-Shirt3',image=ImageFile(io.BytesIO(b'some-file'), name='test-image3.jpg'), description='kl', price=20005)
        product_qs = Products.objects.all()
        srz = ProductSerializer(product_qs, many=True)
        self.assertIsInstance(srz.data, list)
        self.assertEqual(len(srz.data), 2)


class ProductCategorySerializerTestCase(TestCase):

    def test_product_category_serializer(self):
        cat1 = Category.objects.create(title='Kalpak')
        srz = ProductCategorySerializer(cat1, many=False)
        expected_data = {
            'id': cat1.id,
            'name': 'Kalpak',
            'products': [],
        }
        result = srz.data
        self.assertEqual(result, expected_data)

    def test_product_category_with_product_serializer(self):
        cat1 = Category.objects.create(title='SI')
        phone = Products.objects.create(title='SI MuCho', image=ImageFile(io.BytesIO(b'some-file'), name='test-image4.jpg'), price=20000,
                                       description='new', category=cat1)

        srz = ProductCategorySerializer(cat1, many=False)
        expected_data = {
            'id': cat1.id,
            'name': 'SI',
            'products': [
                {
                    'id': phone.id,
                    'title': phone.title,
                    'image': phone.image,
                    'description': phone.description,
                    'price': phone.price,
                    'category_name': cat1.title,
                }
            ],
        }
        result = srz.data
        self.assertEqual(result, expected_data)