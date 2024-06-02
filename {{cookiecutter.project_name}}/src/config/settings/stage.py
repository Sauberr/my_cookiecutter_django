from config.settings.base import *  # noqa
from typing import Any, List


DEBUG = False

SECRET_KEY = 'django-secret-key'

ALLOWED_HOSTS: List[Any] = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'