from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):

    def create_user(self, phone_number, otp=None, **extra_fields):
        """Create and return a `User` with an phone number and OTP as the password."""
        if phone_number is None:
            raise TypeError('Users must have a phone number.')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(otp)
        user.save()

        return user

    def create_superuser(self, phone_number, otp=None, **extra_fields):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if phone_number is None:
            raise TypeError('Superusers must have a phone number.')

        user = self.create_user(phone_number, otp)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    """ All the users in Dukaan app.  """

    # username = models.CharField(db_index=True, max_length=255, unique=True)
    phone_number = models.CharField(db_index=True, max_length=23, unique=True, verbose_name='User phone number with 0,+ or spacing')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'

    objects = AccountManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        """
        return self.phone_number

    @property
    def token(self):
        """
        Allows us to get a user's token
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
