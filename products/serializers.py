from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import models
from collections import OrderedDict
from .models import Product
from stores.models import Store


"""
    To get product catalog & categories
    Take storelink as input
    Respond back with the catelog, grouped by categories & sorted by number of products in the category.
"""


class ProductListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        list_rep = OrderedDict()

        for item in iterable:
            child_rep = self.child.to_representation(item)
            k, v = list(child_rep.items()).pop()
            list_rep.setdefault(k, []).append(v)

        return [
            {k: v}
            for k, v in list_rep.items()
        ]


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        list_serializer_class = ProductListSerializer

    def to_representation(self, value):
        return {
            value.category: [{"id": value.id,
                              "name": value.name, }]
        }


"""
seller starts uploading inventory in the form of products and seller.

Take product name, description, MRP, Sale price, image & category as input.
Create product
Respond back with id, name and image.
"""


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, value):
        return {
            "id": value.id,
            "product_uuid": value.product_uuid,
            "name": value.name,
            "image": str(value.image),

        }

    def create(self, validated_data):
        """
        Creates a new product
        """
        # images_data = self.context['request'].FILES.getlist('image')[0]
        store = validated_data.pop('store')
        store_obj = get_object_or_404(Store, id=store.id)
        product = Product.objects.create(store=store_obj, **validated_data)
        return product


class ProductSerializer(serializers.ModelSerializer):
    """ Serializes Store requests and creates a new Dukaan store"""

    class Meta:
        model = Product
        fields = '__all__'
