from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class BaseManager(models.Manager):

    def get_queryset(self):
        """
        :return: Only objects which their is_deleted is False
        """
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        """
        :return: All objects in database
        """
        return super().get_queryset()


class BaseModel(models.Model):
    """
    using for logical delete
    """
    is_deleted = models.BooleanField(verbose_name=_('Is it deleted'), default=False)

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete_it(self):
        self.is_deleted = True
        self.save()


class TimestampMixin(models.Model):
    """
    any kind of time
    """
    creat_timestamp = models.DateTimeField(verbose_name=_('creat timestamp'), auto_now_add=True)
    modify_timestamp = models.DateTimeField(verbose_name=_('modify timestamp'), auto_now=True)
    delete_timestamp = models.DateTimeField(verbose_name=_('delete timestamp'), default=None, null=True, blank=True)

    def logical_delete_timestamp(self):
        if not BaseModel.is_deleted:
            self.delete_timestamp = None
        else:
            self.delete_timestamp = timezone.now()

    def save(self, *args, **kwargs):
        self.logical_delete_timestamp()
        super(TimestampMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class TestModel(TimestampMixin, BaseModel):
    pass
