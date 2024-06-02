from typing import Any, List

from config.settings.base import *  # noqa


DEBUG = True

SECRET_KEY = 'django-secret-key'

ALLOWED_HOSTS: List[Any] = ['*']

# MIDDLEWARE += [] # noqa # something add like debugtoolbar middleware

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = 'static/'