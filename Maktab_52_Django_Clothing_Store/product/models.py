from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from core.models import *
from django.utils.translation import gettext_lazy as _


# def discount_validator():
#     cls = Product
#     if cls.discount.type == '%':
#         if cls.discount.amount > 100:
#             raise ValidationError(_('Your discount can\'t be more than 100%'))
#         else:
#             return True
#     elif cls.discount.type == '$':
#         if cls.discount.amount > cls.price:
#             raise ValidationError(_('Your discount can\'t be more than the price'))
#         else:
#             return True


class Product(BaseModel, TimestampMixin):
    name = models.CharField(verbose_name=_('Name'), max_length=50, help_text=_('Name of the product'))
    price = models.PositiveIntegerField(_('Price'), help_text=_('Input positive amount in Toomaan/1000'))

    leftovers = models.PositiveIntegerField(_('Leftovers'), help_text=_('Input positive amount'))
    sold = models.PositiveIntegerField(verbose_name=_('Sold items'), default=0)

    description = models.CharField(_('Description'), max_length=1000, null=True, blank=True, default=None)
    image = models.FileField(_('Image'), upload_to='ProductImages/', null=True, blank=True, default=None,
                             help_text=_('Image of the product'))

    color = models.CharField(_('Color'), max_length=30, help_text=_('Color of the product'))
    size = models.CharField(_('Size'), max_length=30, null=True, blank=True, default=None,
                            help_text=_('Size of the product (If it has\'nt size, DO NOT fill it)'))

    category = models.ForeignKey(verbose_name=_('Category'), to='Category', on_delete=models.RESTRICT)
    discount = models.ForeignKey(verbose_name=_('Discount'), to='Discount', on_delete=models.RESTRICT, default=None,
                                 null=True, blank=True)
    brand = models.ForeignKey(verbose_name=_('Brand'), to='Brand', on_delete=models.RESTRICT, default=None, null=True,
                              blank=True)

    class Meta:
        ordering = ['category', 'creat_timestamp']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        if self.size:
            return f'{self.id}. {self.name} - {self.color} - {self.size}, ({self.category})'
        else:
            return f'{self.id}. {self.name} - {self.color}, ({self.category})'

    def final_price(self):
        if self.discount:
            if self.discount.type == '%':
                if self.discount.amount > 100:
                    raise ValidationError(_('Your discount can\'t be more than 100%'))
                else:
                    ds = self.price * self.discount.amount // 100
                    return (self.price - ds) * 1000
            elif self.discount.type == '$':
                if self.discount.amount > self.price:
                    raise ValidationError(_('Your discount can\'t be more than the price'))
                else:
                    ds = self.discount.amount
                    return (self.price - ds) * 1000
        else:
            return self.price * 1000


class Category(BaseModel):
    name = models.CharField(verbose_name=_('Name'), help_text=_('Name of the category'), max_length=50)
    parent = models.ForeignKey(verbose_name=_('Parent'), to='self', null=True, blank=True, default=None,
                               related_name='children', on_delete=models.SET_NULL,
                               help_text=_('For example cloth have three parents. Men, Women and Children'))

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        if self.parent:
            return f'{self.name} => {self.parent}'
        else:
            return f'{self.name}'


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
    name = models.CharField(verbose_name=_('Name'), help_text=_('Name of the discount'), max_length=50, blank=True,
                            null=True, default=None)
    amount = models.PositiveIntegerField(_('Discount Amount'), help_text=_('Input positive amount'),
                                         validators=[])

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'

    def __str__(self):
        if self.name:
            return f'{self.name}: {self.amount}{self.type}'
        else:
            return f'{self.amount}{self.type}'
