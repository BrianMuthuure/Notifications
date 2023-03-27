from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import JSONField

from apps.common.enums import SourceTypes
from apps.common.models import SharedModel


class Device(models.Model):
    id = models.AutoField(
        verbose_name="ID", primary_key=True, auto_created=True)
    name = models.CharField(
        max_length=255, verbose_name=_("Name"), blank=True, null=True)
    active = models.BooleanField(
        verbose_name=_("Is active"),
        default=True,
        help_text=_("Inactive devices will not be sent notify"))
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE,
        related_query_name=_("fcmdevice"), )
    date_created = models.DateTimeField(
        verbose_name=_("Creation date"), auto_now_add=True, null=True
    )

    class Meta:
        abstract = True


class DeviceType(models.TextChoices):
    IOS = "ios", "ios"
    ANDROID = "android", "android"
    WEB = "web", "web"


class FCMDevice(Device):
    device_id = models.CharField(
        verbose_name=_("Device ID"),
        blank=True,
        null=True,
        help_text=_("Unique device identifier"),
        max_length=255,
    )
    registration_id = models.TextField(
        verbose_name=_("Registration token"))
    type = models.CharField(
        choices=DeviceType.choices,
        default=DeviceType.WEB,
        max_length=10,
        verbose_name=_("Device type")
    )

    class Meta:
        verbose_name = _("FCM device")
        verbose_name_plural = _("FCM devices")
        indexes = [
            models.Index(fields=["device_id"])
        ]

    def __str__(self):
        return (self.name or (
                getattr(self, "device_id")
                or "")
                or f"{self.__class__.__name__} for {self.user or 'unknown user'}")


class NotificationTemplate(SharedModel):
    id = models.AutoField(
        verbose_name=_("Notification template ID"),
        primary_key=True,
        auto_created=True,
    )
    message = models.TextField(
        max_length=1000,
        verbose_name=_("message"),
        blank=True,
    )

    details = JSONField(
        encoder=None,
        blank=True,
        null=True
    )
    source = models.CharField(
        choices=SourceTypes.choices,
        default=SourceTypes.DEFAULT,
        max_length=255,
        verbose_name=_("source_type"),
        help_text=_(
            "Identifies the entity associated "
            "with the notification. service identity"
        )
    )
    source_type = models.CharField(
        max_length=1000,
        verbose_name=_("source_type"),
        blank=True,
        help_text=_(
            "The description for the source. "
            "i.e. Maturity follow up Auto-renew ON "
        )
    )
    status = models.BooleanField(
        verbose_name=_("Is Active"),
        default=False,
        help_text=_("True or False"),
    )

    class Meta:
        indexes = [
            models.Index(fields=['source']),
            models.Index(fields=['source_type']),
        ]
        verbose_name = _('Notification Template')
        verbose_name_plural = _('Notification Templates')

    def __str__(self):
        return f"{self.id}: {self.source}" \
            if self.id else "unknown template"
