from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*', 'domain.com', 'www.domain.com']

# Debug-toolbar
if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + [
        'debug_toolbar',  # Debug-toolbar
    ]

    MIDDLEWARE = MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',  # Debug-toolbar
    ]

    INTERNAL_IPS = ['135.125.133.66']

# Database Postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}



# Mailgun Email settings
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_EMAIL = 'NOME <email@email.com>'
