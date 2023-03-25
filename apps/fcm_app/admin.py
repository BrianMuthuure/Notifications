from django.contrib import admin
from django.contrib.auth.models import User

from apps.fcm_app.models import FCMDevice


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
    raw_id_fields = ("user", )
    list_select_related = ("user", )

    def get_search_fields(self, request):
        if hasattr(User, "USERNAME_FIELD"):
            return "name", "device_id", f"user__{User.USERNAME_FIELD}"
        else:
            return "name", "device_id"


admin.site.register(FCMDevice, DeviceAdmin)
