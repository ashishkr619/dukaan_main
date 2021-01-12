from django.db import models
import uuid
from accounts.models import Account
from django.template.defaultfilters import slugify
from random import randrange
# from datetime import datetime


class TimestampedModel(models.Model):
    """ An abstract timestamp model when this object was
        created or updated"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at', '-created_at']


class Store(TimestampedModel):
    """
    A model to store Dukaan Store info.
    1 Customer can have multiple Stores
    """
    customer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='stores')
    store_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique Identifier of each store')
    store_link = models.CharField(max_length=255, blank=True, null=True, unique=True, verbose_name='unique Store Link')
    name = models.CharField(max_length=125, verbose_name='Store name')
    address = models.CharField(max_length=255, verbose_name='Street Address')
    zip_code = models.CharField(max_length=10, verbose_name='Zip Code')
    city = models.CharField(max_length=10, verbose_name='City name of Store')
    country = models.CharField(max_length=20, verbose_name='Store Country')
    is_deleted = models.BooleanField(default=False, verbose_name='Soft delete an store ?')

    class Meta:
        verbose_name = ("store")
        verbose_name_plural = ("stores")
        ordering = ('-name',)

    def clean(self):
        super(Store, self).clean()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        number = randrange(10000)
        string = "%s-%s" % (self.name, number)
        self.store_link = slugify(string)
        super(Store, self).save()
