from django.test import TestCase

# Create your tests here.
from customer.models import User
from order.models import *
from product.models import *


class OrderTest(TestCase):

    def setUp(self) -> None:
        self.category_parent1 = Category.objects.create(name='men', parent_id=None)

        self.category1 = Category.objects.create(name='cloth', parent_id=self.category_parent1.id)

        self.product1 = Product.objects.create(
            name='hoody',
            price=50,
            leftovers=100,
            color='gray',
            size='23',
            category=self.category1,
        )

        self.product2 = Product.objects.create(
            name='hoody',
            price=80,
            leftovers=100,
            color='red',
            size='23',
            category=self.category1,
        )

        self.user1 = User.objects.create(
            first_name='changiz',
            last_name='changiz',
            phone='09123456799',
            password='akbar1234',

        )

        self.order1 = Order.objects.create(
            user=self.user1,
        )

        self.order_item1 = OrderItem.objects.create(
            order=self.order1,
            product=self.product1,
            number=2
        )

        self.order_item2 = OrderItem.objects.create(
            order=self.order1,
            product=self.product2,
            number=1
        )

    def test_meaningless(self):
        self.assertEqual(self.order_item1.number, 2)

    def test_item_price(self):
        print(self.order_item1.item_price())
        self.assertEqual(self.order_item1.item_price(), 100_000)

    def test_total_price(self):
        self.assertEqual(self.order1.total_price(), 180_000)

    def test_total_items(self):
        self.assertEqual(self.order1.total_items(), 3)
