from django.contrib import admin
from rangefilter.filters import DateTimeRangeFilter

from .models import UserEmailLogs


class UserEmailLogsAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_type', 'created_at')
    list_filter = [
        'user',
        'email_type',
        ('created_at', DateTimeRangeFilter),
        ("updated_at", DateTimeRangeFilter),
    ]
    search_fields = ('created_at',)
    date_hierarchy = 'created_at'

    fieldsets = (
        (None, {
            'fields': ('user', 'email_type', 'email_content')
        }),
        (
            'Date Information', {
                'fields': ('created_at',),
                'classes': ('collapse',)
            }
        )
    )


admin.site.register(UserEmailLogs, UserEmailLogsAdmin)
