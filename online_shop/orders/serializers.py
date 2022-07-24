from orders.models import Order
from products.models import Product
from rest_framework import serializers
from users.serializers import UserSerializer


class CartAddProductSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    qty = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CreateOrderSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    total_price = serializers.IntegerField()
