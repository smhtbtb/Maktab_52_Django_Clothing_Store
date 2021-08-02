from django.db import models

# Create your models here.
from core.models import *
from django.utils.translation import gettext as _


class Product(BaseModel, TimestampMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=50, help_text=_('Name of the product'))
    price = models.PositiveIntegerField(_('Price'), help_text=_('Input positive amount in Toomaan/1000'))
    leftovers = models.PositiveIntegerField(_('Leftovers'), help_text=_('Input positive amount'))
    description = models.CharField(_('Description'), max_length=1000)
    image = models.FileField(_('Image'), upload_to='ProductImages/', null=True, blank=True, default=None,
                             help_text=_('Image of the product'))
    color = models.CharField(_('Color'), max_length=30, help_text=_('Color of the product'))
    size = models.CharField(_('Size'), max_length=30,
                            help_text=_('Size of the product (If it has\'nt size, DO NOT fill it)'))
    category = models.ForeignKey(_('Category'), 'Category', on_delete=models.RESTRICT)
    discount = models.ForeignKey(_('Discount'), 'Discount', on_delete=models.RESTRICT, default=None, null=True,
                                 blank=True)
    brand = models.ForeignKey(_('Brand'), 'Brand', on_delete=models.RESTRICT, default=None, null=True, blank=True)

    class Meta:
        ordering = ['category', 'creat_timestamp']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.id}. {self.name}'

    def final_price(self):
        pass


class Category(BaseModel):
    name = models.CharField(verbose_name=_('Name'), help_text=_('Name of the category'), max_length=50)
    parent = models.ForeignKey(_('Parent'), 'self', null=True, blank=True, default=None, related_name=_('children'),
                               on_delete=models.SET_NULL,
                               help_text=_('For example cloth have three parents. Men, Women and Children'))

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name} => {self.parent}'


class Brand(BaseModel):
    name = models.CharField(verbose_name=_('Name'), help_text=_('Name of the brand'), max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return f'{self.name}'


class Discount(BaseModel):
    DISCOUNT_CHOICES = [
        ('%', _('% (Percent)')),
        ('$', _('$ (Toomaan)')),
    ]

    type = models.CharField(verbose_name=_('Type'), max_length=1, choices=DISCOUNT_CHOICES,
                            help_text=_('Type of the discount (percent% or amount$)'))
    name = models.CharField(verbose_name=_('Name'), help_text=_('Name of the discount'), max_length=50)
    amount = models.PositiveIntegerField(_('Discount Amount'), help_text=_('Input positive amount'),
                                         validators=[gt_100_percent()])

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        return f'{self.name}: {self.amount}{self.type}'
