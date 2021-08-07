from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from product.models import Product, Category, Brand, Discount


# TODO: never happens these functions (All Errors)
# class ValidatorTest(TestCase):
#
#     def setUp(self) -> None:
#         self.category_parent1 = Category.objects.create(
#             name='men',
#             parent_id=None
#         )
#
#         self.category1 = Category.objects.create(
#             name='cloth',
#             parent_id=self.category_parent1.id
#         )
#
#         self.brand = Brand.objects.create(
#             name='adidas'
#         )
#
#         self.discnt_percent1 = Discount.objects.create(
#             amount=20,
#             type='%'
#         )
#
#         self.discnt_toomaan1 = Discount.objects.create(
#             amount=20,
#             type='$'
#         )
#
#     def test_negative_price(self):
#         self.product = Product.objects.create(
#             name='hoody',
#             price=-50,
#             leftovers=100,
#             description='nice cloth for cold days',
#             color='gray',
#             size='23',
#             category=self.category1,
#             brand=self.brand,
#         )
#
#         # self.assertRaises(ValidationError)
#
#     def test_negative_discount(self):
#         self.discnt_toomaan_negative = Discount.objects.create(
#             name=None,
#             amount=-20,
#             parent_id=2
#         )
#         self.product = Product.objects.create(
#             name='hoody',
#             price=50,
#             leftovers=100,
#             description='nice cloth for cold days',
#             color='gray',
#             size='23',
#             category=self.category1,
#             discount=self.discnt_toomaan_negative,
#             brand=self.brand,
#         )
#
#     def test_negative_leftovers(self):
#         self.product = Product.objects.create(
#             name='hoody',
#             price=50,
#             leftovers=-100,
#             description='nice cloth for cold days',
#             color='gray',
#             size='23',
#             category=self.category1,
#             brand=self.brand,
#         )
#
#     def test_none_category(self):
#         self.product = Product.objects.create(
#             name='hoody',
#             price=50,
#             leftovers=100,
#             color='gray',
#             size='23',
#         )
#
#     def test_discount_gt100_percent(self):
#         self.discnt_prcnt = Discount.objects.create(
#             name=None,
#             amount=101,
#             parent_id=1
#         )
#         self.product = Product.objects.create(
#             name='hoody',
#             price=50,
#             leftovers=100,
#             description='nice cloth for cold days',
#             color='gray',
#             size='23',
#             category=self.category1,
#             discount=self.discnt_prcnt,
#             brand=self.brand,
#         )


class ProductModelsTest(TestCase):

    def setUp(self) -> None:

        self.category_parent1 = Category.objects.create(
            name='men',
            parent_id=None
        )

        self.category1 = Category.objects.create(
            name='cloth',
            parent_id=self.category_parent1.id
        )

        self.brand = Brand.objects.create(
            name='adidas'
        )

        self.discnt_percent1 = Discount.objects.create(
            amount=20,
            type='%'
        )

        self.discnt_toomaan1 = Discount.objects.create(
            amount=20,
            type='$'
        )

        self.product1 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            color='gray',
            size='23',
            category=self.category1,
            discount=self.discnt_toomaan1,
            brand=self.brand,
        )

        self.product2 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            color='gray',
            size='23',
            category=self.category1,
            discount=self.discnt_percent1,
            brand=self.brand,
        )

        self.product3 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            color='gray',
            size='23',
            category=self.category1,
            brand=self.brand,
        )

        self.product4 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            color='gray',
            size='23',
            category=self.category1,
            brand=self.brand,
        )

        self.product5 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            color='gray',
            size='23',
            category=self.category1,
        )

    def test_final_price_toomaan(self):
        self.assertEqual(self.product1.final_price(), 30_000)

    def test_final_price_percent(self):
        self.assertEqual(self.product2.final_price(), 40_000)

    def test_final_price_without_discnt(self):
        self.assertEqual(self.product3.final_price(), 50_000)

    def test_final_price_without_description(self):
        self.assertEqual(self.product4.final_price(), 50_000)

    def test_final_price_without_brand(self):
        self.assertEqual(self.product5.final_price(), 50_000)

