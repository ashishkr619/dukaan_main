from django.contrib import admin
from .models import Cart, Order


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'cart_uuid', 'product', 'quantity', ]
    list_filter = ['user', 'product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_uuid', 'cart', 'paid', ]
    list_filter = ['cart', 'order_uuid', 'paid']
