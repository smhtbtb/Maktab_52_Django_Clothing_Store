from django.test import TestCase

# Create your tests here.
from customer.models import *


class CustomerTest(TestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(
            first_name='changiz',
            last_name='changiz',
            phone='09123456789',
            password='akbar1234',
            username='sa'

        )

        self.user2 = User.objects.create(
            first_name='changiz',
            last_name='changiz',
            phone='09123456457578',
            password='akbar1234',

        )

    def test1_meaningless(self):
        self.assertEqual(self.user1.first_name, 'changiz')

    # def test2_meaningless(self):
    #     self.assertRaisesRegex(ValidationError, self.user2)
