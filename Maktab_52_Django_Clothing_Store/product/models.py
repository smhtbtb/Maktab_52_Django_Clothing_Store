from django.db import models

# Create your models here.
from core.models import *
from django.utils.translation import gettext as _


class Product(BaseModel, TimestampMixin):
    name = models.CharField(verbose_name=_('name'))
    price = models.PositiveIntegerField()
    leftovers = models.PositiveIntegerField()
    description = models.CharField(max_length=1000)
    image = models.FileField()
    color = models.CharField()
    size = models.CharField()
    category = models.ForeignKey('Category', on_delete=models.RESTRICT)
    discount = models.ForeignKey('Discount', on_delete=models.RESTRICT)
    brand = models.ForeignKey('Brand', on_delete=models.RESTRICT)

    class Meta:
        pass

    def __str__(self):
        pass


class Category(BaseModel):
    name = models.CharField(verbose_name=_('name'), help_text=_('name of the category'))
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name=_('children'),
                               on_delete=models.SET_NULL)

    class Meta:
        pass

    def __str__(self):
        pass


class Brand(BaseModel):
    name = models.CharField(verbose_name=_('name'), help_text=_('name of the brand'))

    class Meta:
        pass

    def __str__(self):
        pass


class Discount(BaseModel):
    DISCOUNT_CHOICES = [
        ('P', _('Percent')),
        ('A', _('Amount')),
    ]

    type = models.CharField(max_length=4, choices=DISCOUNT_CHOICES, default=None, null=True, blank=True,
                            verbose_name=_('type'), help_text=_('type of the discount'))
    name = models.CharField(verbose_name=_('name'), help_text=_('name of the discount'))
    parent = models.ForeignKey('self', null=True, blank=True, default=None, related_name=_('children'),
                               on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField()

    class Meta:
        pass

    def __str__(self):
        pass
