# from django.contrib import admin
from django.contrib import admin
from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'is_active', 'is_staff', ]
