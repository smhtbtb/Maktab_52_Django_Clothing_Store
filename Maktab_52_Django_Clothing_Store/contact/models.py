from django.db import models
from core.models import BaseModel, TimestampMixin
from django.utils.translation import gettext_lazy as _


# Contact model that is not depend on login
class Contact(BaseModel, TimestampMixin):
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(verbose_name=_('Subject'), max_length=150,
                               help_text=_('Tell me what your message is about'))
    message = models.TextField(verbose_name=_('Message'), help_text=_('Write your message here'))

    def __str__(self):
        return self.email
