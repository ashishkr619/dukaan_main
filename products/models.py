import uuid
from django.db import models
from stores.models import Store


class TimestampedModel(models.Model):
    """ An abstract timestamp model when this object was
        created or updated"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at', '-created_at']


class Product(TimestampedModel):
    """ Model to store product info """
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    product_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Product UUID')
    category = models.CharField(max_length=120, verbose_name='Product Categories')
    name = models.CharField(max_length=120, db_index=True, verbose_name='Product name')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='Product description')
    mrp = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='MRP Price ex-23.99')
    sale_price = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Sale Price ex-20.99')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return str(self.name)
