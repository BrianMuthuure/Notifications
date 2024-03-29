# Generated by Django 4.1.7 on 2023-03-26 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmailLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email_type', models.CharField(choices=[('successful_investment', 'Successful Investment'), ('email_verification', 'Email Verification'), ('password_reset', 'Password Reset'), ('password_create', 'Password Create'), ('successful_accreditation', 'Successful Accreditation'), ('failed_accreditation', 'Failed Accreditation'), ('password_changed', 'Password Changed'), ('complete_account', 'Complete Account'), ('kyc_reminder', 'KYC Reminder'), ('start_investing', 'Start Investing'), ('accreditation_nudge', 'Accreditation Nudge'), ('pending_purchase', 'Pending Purchase'), ('rollover_on_reminder_one', 'Rollover on Reminder One'), ('rollover_on_reminder_two', 'Rollover on Reminder Two'), ('nudge_one', 'Nudge One'), ('nudge_two', 'Nudge Two'), ('confirm_ach_investment', 'Confirm ACH Investment'), ('failed_ach_transfer', 'Failed ACH Transfer'), ('provide_bank_details', 'Provide Bank Details'), ('bank_details_present', 'Bank Details Present'), ('bank_details_absent', 'Bank Details Absent')], help_text='The type of email that was sent', max_length=200)),
                ('email_content', models.JSONField(help_text='The JSON data representing the content of the email')),
                ('user', models.ForeignKey(help_text='The user who received the email', on_delete=django.db.models.deletion.CASCADE, related_name='email_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User email log',
                'verbose_name_plural': 'User email logs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='useremaillogs',
            index=models.Index(fields=['-created_at'], name='emails_user_created_7bbc15_idx'),
        ),
    ]
