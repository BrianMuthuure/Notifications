from django.db import models
from django.db.models import JSONField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .enums import NotificationTypes


class SharedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Notification(SharedModel):
    id = models.AutoField(
        verbose_name=_('ID'), primary_key=True, )
    uuid = models.CharField(
        max_length=200, blank=True, verbose_name=_("UUID"))
    type = models.CharField(
        choices=NotificationTypes.choices,
        default=NotificationTypes.GENERAL,
        max_length=1000,
        verbose_name=_('Type'),
        blank=True,
        help_text=_("The type the of notification")
    )
    details = JSONField(blank=True, null=True)
    fcm_response = JSONField(blank=True, null=True)

    class Meta:
        abstract = True
