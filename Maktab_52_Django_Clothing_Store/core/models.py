from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


# Create your models here.

class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    is_deleted = models.BooleanField(verbose_name=_('is it deleted'), default=False)

    objects = BaseManager()

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    creat_timestamp = models.DateTimeField(verbose_name=_('creat timestamp'), auto_now_add=True)
    modify_timestamp = models.DateTimeField(verbose_name=_('modify timestamp'), auto_now=True)
    delete_timestamp = models.DateTimeField(verbose_name=_('delete timestamp'), default=None, null=True, blank=True)

    # def logical_delete_timestamp(self):
    #     if self.is_deleted:
    #         self.delete_timestamp = timezone.now()
    #         self.save()
    #     else:
    #         self.delete_timestamp = None
    #         self.save()

    class Meta:
        abstract = True


class TestModel(TimestampMixin, BaseModel):
    pass
