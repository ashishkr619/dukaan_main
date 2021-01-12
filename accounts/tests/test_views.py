import json
from django.test import TestCase, Client
from django.urls import reverse
# from rest_framework.test import APIRequestFactory
from rest_framework import status

from ..models import Account
from ..serializers import RegistrationSerializer


# initialize the APIClient app
client = Client()


class GetAllUsersTest(TestCase):
    """ Test module for GET all users API """

    def setUp(self):
        self.account_one = Account.objects.create(
            phone_number='56755787899', is_active=False, password='5658')

    def test_list_all_accounts(self):
        # get API response
        response = client.get(
            '/users/')
        # get data from db
        accounts = Account.objects.filter(is_active=False)
        serializer = RegistrationSerializer(accounts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleAccountTest(TestCase):
    """ Test module for GET single account API """

    def setUp(self):
        self.account_one = Account.objects.create(
            phone_number='56755787899', is_active=False, password='5658')

        self.account_two = Account.objects.create(
            phone_number='978676454671', is_active=False, password='4546')

    def test_get_valid_single_account(self):
        response = client.get(
            reverse('account-detail', kwargs={'pk': self.account_two.pk}))
        account = Account.objects.get(pk=self.account_two.pk)
        serializer = RegistrationSerializer(account)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_account(self):
        response = client.get(
            reverse('account-detail', kwargs={'pk': 4330}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewAccountTest(TestCase):
    """ Test module for inserting a new account """

    def setUp(self):
        self.valid_payload = {
            'phone_number': '978676454671',
            'password': '56757'
        }
        self.invalid_payload = {
            'password': '6786'
        }

    def test_create_valid_account(self):
        response = client.post(
            reverse('account-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_account(self):
        response = client.post(
            reverse('account-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
