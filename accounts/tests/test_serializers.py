from django.test import TestCase
from ..serializers import RegistrationSerializer
# from . import models_factories as mfactories
from ..models import Account


class AccountSerializerTest(TestCase):
    def setUp(self):
        self.account_attributes = {
            'phone_number': '56755787899',
            'is_active': False,
            'password': '2568'
        }

        self.account = Account.objects.create(**self.account_attributes)
        self.serializer = RegistrationSerializer(instance=self.account)

    def test_contains_expected_fields(self):

        data = self.serializer.data

        keys = [
            'phone_number',
            'password',
            'token',
        ]

        self.assertEqual(set(data.keys()), set(keys))

    def test_phone_number_field_content(self):

        data = self.serializer.data
        self.assertEqual(data['phone_number'], self.account_attributes['phone_number'])
