from django.db import models
from ..common.models import SharedModel
from django.contrib.auth.models import User
from .enums import EmailType


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
        verbose_name = "User email log"
        verbose_name_plural = "User email logs"

    def __str__(self):
        return f"{self.user.first_name} - {self.email_type}"

