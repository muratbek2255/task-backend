from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from orders.models import OrderItem
from products.models import Products, Category
from users.models import CustomUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'title', 'price')


class ProductCategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)
    name = serializers.CharField(source='title')

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
       )

        user.set_password(validated_data['password'])
        user.save()

        return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('products', 'order')
