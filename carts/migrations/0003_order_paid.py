# Generated by Django 2.2.17 on 2021-01-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Paid T/F'),
        ),
    ]