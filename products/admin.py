# from django.contrib import admin
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'mrp', 'sale_price', 'created_at', 'updated_at']
    list_filter = ['mrp', 'sale_price', 'created_at', 'updated_at']
    list_editable = ['sale_price']
