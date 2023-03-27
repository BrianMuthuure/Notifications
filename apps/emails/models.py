from django.db import models

from ..common.enums import NotificationStatuses
from ..common.models import SharedModel, Notification
from django.contrib.auth.models import User
from .enums import EmailType
from ..fcm_app.models import NotificationTemplate
from django.utils.translation import gettext_lazy as _


class UserEmailLogs(SharedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="email_logs",
        help_text="The user who received the email"
    )
    email_type = models.CharField(
        choices=EmailType.choices,
        max_length=200,
        help_text="The type of email that was sent"
    )
    email_content = models.JSONField(
        encoder=None,
        help_text="The JSON data representing the content of the email"
    )

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"])
        ]
        verbose_name = _("User email log")
        verbose_name_plural = _("User email logs")

    def __str__(self):
        return f"{self.user.first_name} - {self.email_type}"


class EmailNotification(Notification):
    template = models.ForeignKey(
        NotificationTemplate,
        on_delete=models.CASCADE,
        related_name="email_templates"
    )
    status = models.CharField(
        choices=NotificationStatuses.choices,
        default=NotificationStatuses.PENDING,
        max_length=100
    )

    class Meta:
        indexes = [models.Index(fields=["status"])]
        verbose_name = _("Email Notification")
        verbose_name_plural = _("Email Notifications")

    def __str__(self):
        return f"{self.id} {self.type}"
