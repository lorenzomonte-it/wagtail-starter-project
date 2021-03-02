from .base import *
from debug_toolbar.panels import request

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = INSTALLED_APPS + [
    'wagtail.contrib.styleguide',  # Wagtail-Styleguide UI
]

# Database locale Postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}


# Dev environment for test
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'Developer <email@email.com>'
