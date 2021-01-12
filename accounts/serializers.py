from rest_framework import serializers
from .models import Account


"""
seller signs up using his mobile number that creates an account

Take mobile number & OTP (random) as input to the API
Create customer account in accounts table.
Issue a token.
"""


class RegistrationSerializer(serializers.ModelSerializer):
    """ Serializes Registration requests and creates a new user"""

    class Meta:
        model = Account
        fields = ['phone_number', 'password', 'token']

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """ Logins a User with Phone number and OTP """
    phone_number = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number', None)
        # password = data.get('password', None)

        # Raise an exception if an
        # phone_number is not provided.
        if phone_number is None:
            raise serializers.ValidationError(
                'An phone number is required to log in.'
            )
        try:
            # need to write custom generate Otp and verify OTP function.
            user = Account.objects.get(phone_number=phone_number)
        except Account.DoesNotExist:
            raise serializers.ValidationError(
                'A user with this phone number was not found.'
            )
        return {
            'phone_number': user.phone_number,
            'token': user.token
        }
