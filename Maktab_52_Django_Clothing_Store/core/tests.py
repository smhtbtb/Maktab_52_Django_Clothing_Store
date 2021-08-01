from django.test import TestCase

# Create your tests here.
from core.models import TestModel


class BaseModelTest(TestCase):

    def setUp(self) -> None:
        self.m = TestModel.objects.create()

    def test_logical_delete_all(self):
        self.m.is_deleted = True
        self.m.save()

        self.assertNotIn(self.m, TestModel.objects.all())

    def test_logical_delete_filter(self):
        self.m.is_deleted = True
        self.m.save()

        self.assertNotIn(self.m, TestModel.objects.filter())

    def test_logical_delete_get(self):
        self.m.is_deleted = True
        self.m.save()

        self.assertRaises(Exception, TestModel.objects.get, id=1)

    def test_archive(self):
        self.m.is_deleted = True
        self.m.save()

        self.assertIn(self.m, TestModel.objects.archive())


