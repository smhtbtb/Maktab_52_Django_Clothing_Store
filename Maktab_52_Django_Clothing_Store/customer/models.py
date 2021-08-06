from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

# Create your models here.
from core.models import BaseModel


class MyUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    objects = MyUserManager()

    phone = models.CharField(max_length=11, unique=True)
    invite_code = models.CharField(max_length=15, null=True, blank=True, default=True)


class Address(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)

    lat = models.FloatField()
    lng = models.FloatField()

    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)

    detail = models.CharField(max_length=100, null=True, blank=True, default=True)
