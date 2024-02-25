"""
    This is the base settings for both local and production
"""

from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'secretkey'

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
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # my custom context_processors:
                'home_app.context_ps.get_general_site_info',
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
DEFAULT_FILE_STORAGE = ''
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY =''
AWS_S3_ENDPOINT_URL = ''
AWS_STORAGE_BUCKET_NAME = ''
AWS_SERVICE_NAME = 's3' #optional
AWS_S3_FILE_OVERWRITE = False #don't over write files wiht same name
