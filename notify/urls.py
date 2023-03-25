from decouple import config
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title=config("API_TITLE"),
        default_version=config("API_VERSION"),
        description=config("API_DESCRIPTION"),
        terms_of_service=config("TnCS_URL"),
        contact=openapi.Contact(email=config("CONTACT_EMAIL")),
        x_logo={"url": config("LOGO_URL"), "backgroundColor": "#FFFFFF"}
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('developer/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('developer/doc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]

admin.site.site_header = config('ADMIN_SITE_HEADER')
admin.site.site_title = config('ADMIN_SITE_TITLE')
admin.site.index_title = config('ADMIN_SITE_INDEX_TITLE')
