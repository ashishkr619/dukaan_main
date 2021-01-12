# Generated by Django 2.2.17 on 2021-01-09 17:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Product UUID')),
                ('category', models.CharField(max_length=120, unique=True, verbose_name='Product Categories')),
                ('name', models.CharField(db_index=True, max_length=120, verbose_name='Product name')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Product description')),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='MRP Price ex-23.99')),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sale Price ex-20.99')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stores.Store')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]