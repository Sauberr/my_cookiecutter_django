from typing import Any, List

from config.settings.base import *  # noqa


DEBUG = True

SECRET_KEY = 'django-secret-key'

ALLOWED_HOSTS: List[Any] = ['*', '127.0.0.1']

# MIDDLEWARE += [] # noqa # something add like debugtoolbar middleware

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'

MEDIA_ROOT = (BASE_DIR / 'media')

STATIC_ROOT = (BASE_DIR / 'staticfiles')
