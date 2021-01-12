# Generated by Django 2.2.17 on 2021-01-10 14:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique Identifier of each order')),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Final Price of item')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='carts.Cart')),
            ],
            options={
                'ordering': ['-order_uuid'],
            },
        ),
    ]