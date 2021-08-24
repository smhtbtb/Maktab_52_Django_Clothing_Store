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
            phone='091234567899',
            password='akbar1234',

        )

        self.address1 = Address.objects.create(
            owner=self.user1,
            city='kashoon',
            province='kashoonak'
        )

        self.address2_bad = Address.objects.create(
            owner=self.user1,
            city='kashoon',
            province='kashoonak',
            post_code='123'
        )

        self.address3_bad_user = Address.objects.create(
            owner=self.user2,
            city='kashoon',
            province='kashoonak'
        )

    def test1_meaningless(self):
        self.assertEqual(self.user1.first_name, 'changiz')

    # def test2_meaningless(self):
    #     # self.assertRaises(ValidationError, self.user2.phone)
    #     # self.assertRaisesRegex(ValidationError, 'Invalid phone number', self.user2.phone)
    #     self.assertRaisesRegex(ValidationError, "invalid phone number", self.user2.phone)

    def test3_address(self):
        self.assertEqual(self.address1.province, 'kashoonak')

    # def test4_address_bad_post_code(self):
    #     self.assertRaises(ValidationError, self.address2_bad)

    def test5_address_bad_user(self):
        self.assertEqual(self.address3_bad_user.province, 'kashoonak')

