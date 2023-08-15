"""
    use for production
"""
from core.settings.base import *
import os

DEBUG = False
ALLOWED_HOSTS = []

# Database connection to Azure URL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

## For django storages
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
