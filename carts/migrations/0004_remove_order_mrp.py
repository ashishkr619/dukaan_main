# Generated by Django 2.2.17 on 2021-01-10 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_order_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='mrp',
        ),
    ]
