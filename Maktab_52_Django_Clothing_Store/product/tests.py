from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from product.models import Product, Category, Brand, Discount


# TODO: never happens these functions (All Errors)
class ValidatorTest(TestCase):

    def setUp(self) -> None:
        self.category_parent1 = Category.objects.create(
            name='men',
            parent_id=None
        )

        self.category1 = Category.objects.create(
            name='cloth',
            parent_id=Category.objects.get(id=1)
        )

        self.brand = Brand.objects.create(
            name='adidas'
        )

        self.discnt_parent1 = Discount.objects.create(
            name='percent',
            amount=None,
            parent_id=None
        )

        self.discnt_parent2 = Discount.objects.create(
            name='toomaan',
            amount=None,
            parent_id=None
        )

        self.discnt_percent1 = Discount.objects.create(
            name=None,
            amount=20,
            parent_id=Discount.objects.get(id=1)
        )

        self.discnt_toomaan1 = Discount.objects.create(
            name=None,
            amount=20,
            parent_id=Discount.objects.get(id=2)
        )

    def test_negative_price(self):
        self.product = Product.objects.create(
            name='hoody',
            price=-50,
            leftovers=100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=None,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

    def test_negative_discount(self):
        self.discnt_toomaan_negative = Discount.objects.create(
            name=None,
            amount=-20,
            parent_id=2
        )
        self.product = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=self.discnt_toomaan_negative,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

    def test_negative_leftovers(self):
        self.product = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=-100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=None,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

    def test_none_category(self):
        self.product = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description=None,
            image=None,
            color='gray',
            size='23',
            category=None,
            discount=None,
            brand=None,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

    def test_discount_gt100_percent(self):
        self.discnt_prcnt = Discount.objects.create(
            name=None,
            amount=101,
            parent_id=1
        )
        self.product = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=self.discnt_prcnt,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )


class ProductModelsTest(TestCase):

    def setUp(self) -> None:
        self.product1 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=self.discnt_toomaan1,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

        self.product2 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=self.discnt_percent1,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

        self.product3 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description='nice cloth for cold days',
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=None,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

        self.product4 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description=None,
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=None,
            brand=self.brand,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

        self.product5 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            description=None,
            image=None,
            color='gray',
            size='23',
            category=self.category1,
            discount=None,
            brand=None,
            is_deleted=False,
            creat_timestamp=timezone.now(),
            modify_timestamp=timezone.now(),
            delete_timestamp=None,
        )

        self.category_parent1 = Category.objects.create(
            name='men',
            parent_id=None
        )

        self.category1 = Category.objects.create(
            name='cloth',
            parent_id=Category.objects.get(id=1)
        )

        self.brand = Brand.objects.create(
            name='adidas'
        )

        self.discnt_parent1 = Discount.objects.create(
            name='percent',
            amount=None,
            parent_id=None
        )

        self.discnt_parent2 = Discount.objects.create(
            name='toomaan',
            amount=None,
            parent_id=None
        )

        self.discnt_percent1 = Discount.objects.create(
            name=None,
            amount=20,
            parent_id=Discount.objects.get(id=1)
        )

        self.discnt_toomaan1 = Discount.objects.create(
            name=None,
            amount=20,
            parent_id=Discount.objects.get(id=2)
        )

    def test_final_price_toomaan(self):
        self.assertEqual(self.product1.final_price(), 30_000)

    def test_final_price_percent(self):
        self.assertEqual(self.product2.final_price(), 40_000)

    def test_final_price_without_discnt(self):
        self.assertEqual(self.product3.final_price(), 50_000)









