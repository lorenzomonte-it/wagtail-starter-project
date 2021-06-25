from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*', 'domain.com', 'www.domain.com']


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



# Email settings
# EMAIL_HOST = ''
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''

# DEFAULT_FROM_EMAIL = 'NOME <email@email.com>'
