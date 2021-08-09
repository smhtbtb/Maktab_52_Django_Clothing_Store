from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from core.models import *
from customer.models import User
from product.models import Product


# class Status(BaseModel):
#     STATUS_CHOICES = [
#         ('Cn', _('Canceled')),
#         ('Ps', _('Posting')),
#         ('Pr', _('Processing')),
#     ]
#
#     type = models.CharField(verbose_name=_('Type'), max_length=2, choices=STATUS_CHOICES,
#                             help_text=_('Types of the status'), default='Pr')
#
#     def __str__(self):
#         return f'{self.type}'


class Order(BaseModel, TimestampMixin):
    PAYMENT_CHOICES = [
        ('O', _('Online')),
        ('C', _('Card (In-person payment)')),
    ]
    STATUS_CHOICES = [
        ('Cn', _('Canceled')),
        ('Ps', _('Posting')),
        ('Pr', _('Processing')),
    ]

    user = models.ForeignKey(verbose_name=_('User'), to=User, on_delete=models.DO_NOTHING),
    payment_type = models.CharField(verbose_name=_('Payment Type'), max_length=1, choices=PAYMENT_CHOICES, default='O')
    status = models.CharField(verbose_name=_('Status'), max_length=2, choices=STATUS_CHOICES,
                              help_text=_('Types of the status'), default='Pr')

    class Meta:
        ordering = ['creat_timestamp']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.user}, {self.status} ({self.payment_type})'


class OrderItem(BaseModel, TimestampMixin):
    number = models.PositiveIntegerField(default=1),
    order = models.ForeignKey(verbose_name=_('Order'), to=Order, on_delete=models.DO_NOTHING),
    product = models.ForeignKey(verbose_name=_('Product'), to=Product, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['creat_timestamp']
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f'{self.order}=> {self.product}, {self.number}'

    def item_price(self):
        return self.product.final_price
