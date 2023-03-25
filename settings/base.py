import os
import sys
from os.path import abspath, basename, dirname, join, normpath
from decouple import config
from firebase_admin import initialize_app, credentials
from django.core.management.utils import get_random_secret_key

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

BASE_DIR = os.path.normpath(os.path.dirname(__file__))

PROJECT_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)

# Define the path to the secret file
SECRET_FILE_PATH = normpath(join(DJANGO_ROOT, 'secret_file.txt'))

# Try to read the secret key from the file
try:
    with open(SECRET_FILE_PATH) as f:
        SECRET_KEY = f.read().strip()
except FileNotFoundError:
    # If the file doesn't exist, generate a new secret key and save it to the file
    SECRET_KEY = get_random_secret_key()
    with open(SECRET_FILE_PATH, 'w') as f:
        f.write(SECRET_KEY)

# Raise an exception if the secret key couldn't be obtained or saved
if not SECRET_KEY:
    raise Exception(
        f"Could not read or generate the secret key from {SECRET_FILE_PATH}!")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["*"]

sys.path.append(normpath(join(DJANGO_ROOT, 'apps')))

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.fcm_app',
    'apps.bell',
    'apps.emails',
    'apps.slack',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'drf_yasg',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

ROOT_URLCONF = '%s.urls' % SITE_NAME

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
USE_I18N = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Email configurations
EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
SECURITY_EMAIL_SENDER = config('EMAIL_HOST_USER')
EMAIL_USE_TLS = config("EMAIL_USE_TLS")

# Celery details
CELERY_BROKER_URL = config('BROKER_URL')
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ["pickle", config('CELERY_ACCEPT_CONTENT')]
CELERY_TASK_SERIALIZER = config('CELERY_SERIALIZER')
CELERY_RESULT_SERIALIZER = config('CELERY_SERIALIZER')
CELERY_BEAT_SCHEDULER = config('CELERY_BEAT_SCHEDULER')
CELERY_TIMEZONE = config('CELERY_TIMEZONE')

CACHES = {
    "default": {
        "BACKEND": config("REDIS_BACKEND"),
        "LOCATION": config("REDIS_DB_LOCATION"),
        "OPTIONS": {
            "CLIENT_CLASS": config("REDIS_CLIENT_CLASS")
        },
        "KEY_PREFIX": "development"
    }
}

# DJANGO FCM SETTINGS
FCM_DJANGO_SETTINGS = {
    "APP_VERBOSE_NAME": "firebase cloud messaging",
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": False,
}

cred = credentials.Certificate(
    os.path.join(DJANGO_ROOT, config("GOOGLE_APPLICATION_CREDENTIALS")))

FIREBASE_APP = initialize_app(cred)
