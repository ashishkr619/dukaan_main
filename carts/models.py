import uuid
from django.db import models
from accounts.models import Account
from products.models import Product
from django.db.models.signals import post_save


class TimestampedModel(models.Model):
    """ An abstract timestamp model when this object was
        created or updated"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at', '-created_at']


class Cart(TimestampedModel):
    """ Store Cart items for users """
    # Enforce 1 user to have only 1 Cart
    user = models.OneToOneField(Account, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Cart owner')
    # The identifier to identify each cart
    cart_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique Identifier of each cart')
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name='carts', verbose_name='Product')
    quantity = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['-cart_uuid']

    def __str__(self):
        return str(self.user)

    @property
    def get_total_mrp_price(self):
        return self.quantity * self.product.mrp

    @property
    def get_total_sale_price(self):
        return self.quantity * self.product.sale_price

    @property
    def get_amount_saved(self):
        return self.get_total_mrp_price() - self.get_total_sale_price()


def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)


post_save.connect(create_user_cart, sender=Account)


class Order(TimestampedModel):
    """ Create a new product Order """
    order_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique Identifier of each order')
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False, verbose_name='Paid T/F')

    class Meta:
        ordering = ['-order_uuid']

    def __str__(self):
        return str(self.cart)
