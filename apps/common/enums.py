from django.utils.translation import gettext_lazy as _
from django.db import models


class NotificationCategories(models.TextChoices):
    EMAIL = "email", _("Email")
    BELL = "bell", _("Bell")
    EMAIL_BELL = "email_bell", _("Email and Bell")


class SourceTypes(models.TextChoices):
    KYC_AML = "kyc_aml", _("KYC/AML")
    ACCREDITATION = "accreditation", _("Accreditation")
    EMAIL_VERIFICATION = "email_verification", _("Email Verification")
    INVEST = "invest", _("Invest")
    MATURITY = "maturity", _("Maturity")
    PRINCIPAL_PAYMENT = "principal_payment", _("Principal Payment")
    PAYOUT = "payout", _("Payout")
    REWARD = "reward", _("Reward")
    DEFAULT = "default", _("Default")


class NotificationStatuses(models.TextChoices):
    SENT = "sent", _("Sent")
    READ = "read", _("Read")
    PENDING = "pending", _("Pending")
    UNREAD = "unread", _("Unread")


class NotificationTypes(models.TextChoices):
    GENERAL = "general", _("General")
    NOTE_PLACED = "note_placed", _("Note Placed")
    NOTE_MATURITY = "note_maturity", _("Note Maturity")
    NOTE_ROLLOVER = "note_rollover", _("Note Rollover")
    ACCREDITATION_PASSED = "accreditation_passed", _("Accreditation Passed")
    ACCREDITATION_FAILED = "accreditation_failed", _("Accreditation Failed")
    VERIFICATION_FAILED = "verified_failed", _("Verification Failed")
    VERIFICATION_PASSED = "verified_account", _("Verification Passed")
    EMAIL_VERIFIED = "email_verified", _("Email Verified")
    REWARD_AWARDED = "new_rewards", _("New Rewards")
    WELCOMING_REWARD = "welcoming_rewards", _("Welcoming Rewards")
    FORGOT_PASSWORD_REQUEST = "forgot_password_request", _("Forgot Password Request")
    PASSWORD_CHANGED = "password_changed", _("Password Changed")
    PAYOUT_INITIATED = "payout_initiated", _("Payout Initiated")
    AUTO_RENEW_UPDATE = "30_days_to_maturity_auto_renew_update", _("30 Days to Maturity Auto Renew Update")
    MATURITY_AUTO_RENEW_UPDATE = "maturity_auto_renew_update", _("Maturity Auto Renew Update")


class RedirectPrefixes:
    DASHBOARD = "/dashboard"
    PORTFOLIO = f"{DASHBOARD}/my-portfolio"
    COMMUNITY = f"{DASHBOARD}/my-community"


class CxAgentNotificationTypes(models.TextChoices):
    MATURING_NOTES = "maturing_notes", _("Maturing Notes")
