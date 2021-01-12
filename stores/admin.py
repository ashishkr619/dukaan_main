# from django.contrib import admin
from django.contrib import admin
from .models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'store_link', 'name', 'address', ]
    list_filter = ['name', 'address', 'updated_at']
