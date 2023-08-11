"""
Django settings for Severless project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =os.environ.get("DEBUG","False").lower()=="true"

ALLOWED_HOSTS =os.environ.get("ALLOWED_HOSTS").split(" ")
#['po4nwvbvwh.execute-api.us-east-1.amazonaws.com','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
     "corsheaders",
     "django_extensions",
    "app_1",
    "zappa",
    "rest_framework",
    "django_cognito_jwt",
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
     "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': [
#        'rest_framework_simplejwt.authentication.JWTAuthentication',
#    ],
#}

#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'django_cognito_jwt.authentication.CognitoAuthentication',
#    ),
#}
#COGNITO_CONFIG = {
#    'app_client_id': '7g2af98fpbih3tgb28btf3vnkq',
#    'region': 'us-east-1',
#    'user_pool_id': 'us-east-1_LsUhND2zs',
#}
#SIMPLE_JWT = {
#    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
#    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
#}
# settings.py
# Add authentication and permission classes
#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': [
#        'rest_framework_simplejwt.authentication.JWTAuthentication',
#    ],
#    'DEFAULT_PERMISSION_CLASSES': [
#        'rest_framework.permissions.IsAuthenticated',
#    ],
#}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Set the access token lifetime
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Set the sliding token refresh lifetime
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # Set the sliding token refresh lifetime
    'ALGORITHM': 'HS256',  # Specify the token signing algorithm (default: HS256)
    'SIGNING_KEY': SECRET_KEY,  # Use your Django's SECRET_KEY as the signing key
    'AUTH_HEADER_TYPES': ('Bearer',),  # Define accepted auth header types
    'USER_ID_FIELD': 'sub',  # Set the user identifier field (default: 'id')
    'USER_ID_CLAIM': 'sub',  # Set the user identifier claim (default: 'sub')
}

COGNITO_USER_POOL_ID = 'us-east-1_LsUhND2zs'
COGNITO_APP_CLIENT_ID = '7g2af98fpbih3tgb28btf3vnkq'
COGNITO_AWS_REGION='us-east-1'


CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
ROOT_URLCONF = "Severless.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Severless.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATICFILES_DIRS = [
#    BASE_DIR / "static",
#]
# settings.py

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
