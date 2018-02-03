from kiosk.models import Product
from django.test import TestCase


class ProductTest(TestCase):

    def test_str(self):
        product = Product(name='Latte', cost=100)

        self.assertEquals(
            str(product),
            'Latte'
        )
