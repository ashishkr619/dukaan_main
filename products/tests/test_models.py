# import uuid
from django.test import TestCase
from django.core.exceptions import ValidationError
# from PIL import Image
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.utils.six import BytesIO
from ..models import Product
from stores.models import Store
from accounts.models import Account
from django.shortcuts import get_object_or_404
# from . import models_factories as mfactories


class ProductTest(TestCase):
    def setUp(self):
        # self.store_uuid = uuid.uuid4()
        self.user = Account.objects.create(phone_number='944345335', password='1234')
        self.customer_obj = get_object_or_404(Account, id=self.user.id)
        self.store = Store.objects.create(customer=self.customer_obj, name='test store', address='ad1', zip_code='80001', city='Kolkata', country='India')
        self.store_obj = get_object_or_404(Store, id=self.store.id)

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

    def test_product_save_required_fields(self):
        # having issues with Zlib library
        # image = BytesIO()
        # Image.new('RGB', (100, 100)).save(image, 'PNG')
        # image.seek(0)
        # product_image = SimpleUploadedFile('image.png', image.getvalue())
        product = Product.objects.create(
            store=self.store_obj,
            category='shoes', name='Nike shoe', mrp=23.99, sale_price=20.99)
        product_db = Product.objects.get(pk=product.pk)
        self.assertEqual(product_db.name, 'Nike shoe')

    def test_product_save_fails_missing_name(self):
        product = Product.objects.create(
            store=self.store_obj,
            category='shoes', mrp=23.99, sale_price=20.99)

        self.assertRaises(ValidationError, product.full_clean)
