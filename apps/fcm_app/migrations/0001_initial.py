# Generated by Django 4.1.7 on 2023-03-25 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FCMDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('active', models.BooleanField(default=True, help_text='Inactive devices will not be sent notify', verbose_name='Is active')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creation date')),
                ('device_id', models.CharField(blank=True, help_text='Unique device identifier', max_length=255, null=True, verbose_name='Device ID')),
                ('registration_id', models.TextField(verbose_name='Registration token')),
                ('type', models.CharField(choices=[('ios', 'ios'), ('android', 'android'), ('web', 'web')], default='web', max_length=10, verbose_name='Device type')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='fcmdevice', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'FCM device',
                'verbose_name_plural': 'FCM devices',
            },
        ),
        migrations.AddIndex(
            model_name='fcmdevice',
            index=models.Index(fields=['device_id'], name='fcm_app_fcm_device__e70865_idx'),
        ),
    ]
