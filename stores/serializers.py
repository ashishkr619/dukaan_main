from rest_framework import serializers
from .models import Store
from django.shortcuts import get_object_or_404
from accounts.models import Account

"""
seller creates his store

Take store name & address as input.
Create store in store table. One customer can have multiple stores.
Generate a unique store link based on his store name.
Respond back with storeid and link.
"""


class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

    def to_representation(self, value):
        return {
            "id": value.id,
            "store_uuid": value.store_uuid,
            "store_link": value.store_link,
        }


class StoreSerializer(serializers.ModelSerializer):
    """ Serializes Store requests and creates a new Dukaan store"""

    class Meta:
        model = Store
        fields = '__all__'

    def create(self, validated_data):
        """
        Creates a new store
        """
        name = validated_data.pop('name')
        address = validated_data.pop('address')
        zip_code = validated_data.pop('zip_code')
        country = validated_data.pop('country')
        city = validated_data.pop('city')
        customer = validated_data.pop('customer')
        customer_obj = get_object_or_404(Account, id=customer.id)
        store = Store.objects.create(name=name, address=address, zip_code=zip_code, country=country, city=city, customer=customer_obj)
        return store
