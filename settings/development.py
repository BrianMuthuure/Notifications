from .base import *

from .i18n import *

# DATABASE SETTINGS

DATABASES = {
    'default': {
        'ENGINE': config("DEV_DATABASE_ENGINE"),
        'NAME': config("DEV_DATABASE_NAME"),
        'USER': config("DEV_DATABASE_USER"),
        'HOST': config("DEV_DATABASE_HOST"),
        'PASSWORD': config("DEV_DATABASE_PASSWORD"),
        'PORT': config("DEV_DATABASE_PORT"),
    },
}

