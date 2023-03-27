from django.contrib import admin
from django.contrib.auth.models import User
from rangefilter.filters import DateTimeRangeFilter

from apps.fcm_app.models import FCMDevice, NotificationTemplate


class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "device_id",
        "name",
        "type",
        "user",
        "active",
        "date_created",
    )
    list_filter = (
        "active",
        "user",
        "type",
    )
    raw_id_fields = ("user",)
    list_select_related = ("user",)

    def get_search_fields(self, request):
        if hasattr(User, "USERNAME_FIELD"):
            return "name", "device_id", f"user__{User.USERNAME_FIELD}"
        else:
            return "name", "device_id"


admin.site.register(FCMDevice, DeviceAdmin)


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    date_hierarchy = 'created_at'
    search_fields = ("source",)
    list_filter = ["source", ("created_at", DateTimeRangeFilter),
                   ("updated_at", DateTimeRangeFilter), ]
    list_display = ["id", "source", "message", "created_at", "updated_at"]
