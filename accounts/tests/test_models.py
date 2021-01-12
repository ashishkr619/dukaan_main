import uuid
from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Account
# from . import models_factories as mfactories


class AccountTest(TestCase):
    def setUp(self):
        self.room_uuid = uuid.uuid4()

    def assertRaisesWithMessage(self, exc, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except exc as inst:
            self.assertIn(msg, inst.messages)

    def assertRaisesWithMessageDict(self, exc, msg, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
            self.assertFail()
        except exc as inst:
            self.assertEqual(msg, inst.message_dict)

    def test_account_save_required_fields(self):
        account = Account.objects.create(
            phone_number=4352992,
            password=12345)
        account_db = Account.objects.get(pk=account.pk)
        self.assertEqual(account_db.phone_number, '4352992')

    def test_account_save_all_fields(self):
        account = Account.objects.create(
            phone_number=7352992,
            is_active=False,
            is_staff=False)

        account_db = Account.objects.get(pk=account.pk)
        self.assertEqual(account_db.is_active, False)

    def test_account_save_fails_missing_phone_number(self):
        account = Account.objects.create(is_active=False)

        self.assertRaises(ValidationError, account.full_clean)
