from django.http import HttpResponse, Http404
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema

from orders.models import OrderItem
from products.models import Products
from products.serializers import ProductSerializer, UserSerializer, OrderSerializer
from users.models import CustomUser


class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(APIView):
    @swagger_auto_schema(
        operation_summary='Get detail of product',
        responses={
            '200': ProductSerializer(many=False),
            '404': 'Product not found.',
        }
    )
    def get(self, request, pk):
        try:
            product = Products.objects.get(id=pk)
        except Products.DoesNotExist:
            return Response({'message': 'Product not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        srz = ProductSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Delete a product',
        request_body=None,
        responses={'204': None}
    )
    def delete(self, request, pk):
        try:
            product = Products.objects.get(id=pk)
        except Products.DoesNotExist:
            return Response({'message': 'Product not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(
        operation_summary='Update detail of product',
        responses={
            '200': ProductSerializer(many=False),
        },
        request_body=ProductSerializer(many=False)
    )
    def put(self, request, pk):
        request_body = request.data
        try:
            product = Products.objects.get(id=pk)
        except Products.DoesNotExist:
            raise Http404
        product.title = request_body['title']
        product.description = request_body['description']
        product.price = request_body['price']
        product.save()
        srz = ProductSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer
