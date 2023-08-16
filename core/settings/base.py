"""
    This is the base settings for both local and production
"""

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure--u^h@l(p)1hf0-j#s+%^@-&q=&hkx9kjio8qc+z03*t2cz3be*'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party libraries:
    'django_cleanup.apps.CleanupConfig',
    'storages',
    'boto3',
    # local apps:
    'home_app.apps.HomeAppConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'core.urls'

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


WSGI_APPLICATION = 'core.wsgi.application'


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


BASE_DOMAIN = "http://127.0.0.1:8000"


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# storages
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '9d0d0a56-c95c-4391-a85c-4286a25df38e'
AWS_SECRET_ACCESS_KEY ='c87a1273a69f510ea72d747a661b6f8736f2255b4fccebd1a26c0a6040d8dcbe'
AWS_S3_ENDPOINT_URL = 'https://pouria-portfolio.s3.ir-thr-at1.arvanstorage.ir'
AWS_STORAGE_BUCKET_NAME = 'pouria-portfolio'
AWS_SERVICE_NAME = 's3' #optional
AWS_S3_FILE_OVERWRITE = False #don't over write files wiht same name
