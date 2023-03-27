from django.test import TestCase
from django.contrib.auth.models import User

from apps.common.enums import NotificationStatuses
from apps.common.test_data import (
    user_data,
    email_log_data,
    notification_template_data
)
from apps.emails.enums import EmailType
from apps.emails.models import UserEmailLogs, EmailNotification
from apps.fcm_app.models import NotificationTemplate


class UserEmailLogsModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(**user_data)
        self.email_log = UserEmailLogs.objects.create(
            user=self.user, **email_log_data)

    def test_email_log_creation(self):
        self.assertEqual(self.email_log.user, self.user)
        self.assertEqual(
            self.email_log.email_type, EmailType.PASSWORD_RESET)
        self.assertIsNotNone(self.email_log.email_content)
        self.assertIsNotNone(self.email_log.created_at)

    def test_email_log_str_method(self):
        expected_str = f"{self.user.first_name} - {EmailType.PASSWORD_RESET}"
        self.assertEqual(str(self.email_log), expected_str)

    def test_email_log_ordering(self):
        # Create another UserEmailLogs object with a different creation time
        later_email_log = UserEmailLogs.objects.create(
            user=self.user,
            email_type=EmailType.EMAIL_VERIFICATION,
            email_content={"message": "Your account has been verified."}
        )
        expected_ordering = [later_email_log, self.email_log]
        self.assertQuerysetEqual(
            UserEmailLogs.objects.all(),
            expected_ordering, transform=lambda x: x)

    def test_email_log_indexes(self):
        # Ensure that the created_at field is indexed
        self.assertIn("-created_at", UserEmailLogs._meta.indexes[0].fields)

    def test_email_log_verbose_names(self):
        self.assertEqual(UserEmailLogs._meta.verbose_name, 'User email log')
        self.assertEqual(UserEmailLogs._meta.verbose_name_plural, 'User email logs')


class EmailNotificationTestCase(TestCase):

    def setUp(self):
        self.template = NotificationTemplate.objects.create(**notification_template_data)

    def test_str_representation(self):
        email_notification = EmailNotification.objects.create(
            template=self.template,
            status=NotificationStatuses.PENDING
        )
        self.assertEqual(
            str(email_notification),
            f"{email_notification.id} Email Notification"
        )

    def test_template_relationship(self):
        email_notification = EmailNotification.objects.create(
            template=self.template,
            status=NotificationStatuses.PENDING
        )
        self.assertEqual(email_notification.template, self.template)

    def test_default_status(self):
        email_notification = EmailNotification.objects.create(
            template=self.template
        )
        self.assertEqual(
            email_notification.status,
            NotificationStatuses.PENDING
        )

    def test_valid_status_choices(self):
        email_notification = EmailNotification.objects.create(
            template=self.template,
            status=NotificationStatuses.SENT
        )
        self.assertIn(
            email_notification.status,
            [s[0] for s in NotificationStatuses.choices]
        )

    def test_verbose_name_plural(self):
        self.assertEqual(
            str(EmailNotification._meta.verbose_name_plural),
            "Email Notifications"
        )
