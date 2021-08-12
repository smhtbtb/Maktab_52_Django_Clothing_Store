from django.contrib.auth.models import UserManager, AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
import re
from django.utils.translation import gettext_lazy as _

# Create your models here.
from core.models import BaseModel


def phone_validator(val):
    pattern = r"^(\+98|0)?9\d{9}$"

    if not re.match(pattern, val):
        raise ValidationError(_('Your phone number is incorrect'))
    else:
        return val


def post_code(val):
    pattern = r"^\d{10}$"

    if not re.match(pattern, val):
        raise ValidationError(_('Your post code is incorrect'))
    else:
        return val


class MyUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    objects = MyUserManager()

    phone = models.CharField(verbose_name=_('Phone'), max_length=15, unique=True)
    invite_code = models.CharField(verbose_name=_('Invite Code'), max_length=15, null=True, blank=True, default=None,
                                   help_text=_('If you have not invite code do not fill this field'))

    def save(self, *args, **kwargs):
        self.username = str(self.phone)
        super().save(*args, **kwargs)


class Address(BaseModel):
    owner = models.ForeignKey(verbose_name=_('Owner'), to=User, on_delete=models.RESTRICT,
                              help_text=_('The owner of the address'))

    lat = models.FloatField(verbose_name=_('Geographic latitude'), null=True, blank=True, default=None)
    lng = models.FloatField(verbose_name=_('Geographic longitude'), null=True, blank=True, default=None)

    city = models.CharField(verbose_name=_('City'), max_length=20)
    province = models.CharField(verbose_name=_('Province'), max_length=20)

    detail = models.CharField(verbose_name=_('Detail'), max_length=100, null=True, blank=True, default=None,
                              help_text=_('Detail of the address, like alley name or house number'))

    post_code = models.CharField(verbose_name=_('Post Code'), max_length=10, null=True, blank=True, default=None,
                                 help_text=_('Write your 10 character post code'), validators=[post_code])

    def __str__(self):
        return f'{self.city} - {self.province} - {self.detail}'
