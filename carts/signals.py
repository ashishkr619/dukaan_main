# from accounts.models import Account
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import Cart


# @receiver(post_save, sender=Account)
# def create_user_cart(sender, instance, created, **kwargs):
#     if created:
#         Cart.objects.create(user=instance)
