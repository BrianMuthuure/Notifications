from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


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