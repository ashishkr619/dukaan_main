from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Cart, Order


class CartSerializer(serializers.ModelSerializer):
    """ Serializes Cart requests and creates a new cart"""

    class Meta:
        model = Cart
        fields = ['user', 'cart_uuid', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    """ Serializes Order requests and creates a new order"""

    class Meta:
        model = Order
        fields = ['cart', 'order_uuid', 'paid', ]

    def create(self, validated_data):
        """
        Creates a new order
        """
        cart = validated_data.pop('cart')
        cart_obj = get_object_or_404(Cart, id=cart.id)
        # quantity = cart_obj.quantity
        order = Order.objects.create(cart=cart_obj, paid=True)
        return order
