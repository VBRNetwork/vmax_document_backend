"""
Django settings for VBR Document Manager.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from main.handlers import CustomisedJSONFormatter
from pathlib import Path
import datetime
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "%w@7@jdglgm8x#ldrru@%4yt#$dar&l4s7ckwhle7)%r3db2j!"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 2
SITE_PROTOCOL = "https://"
SITE_DOMAIN = "vmax-documents.vbrlabs.io"
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "183.10.0.4",
    "192.168.1.27",
    "192.168.1.211",
    "192.168.1.183",
    "192.168.1.122",
    "api",
    SITE_DOMAIN,
]
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "xxxx"
EMAIL_PORT = 465
EMAIL_HOST_USER = "xxxxx"
EMAIL_HOST_PASSWORD = "xxxxx"
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = "xxxx"
# Application definition

MICROSERVICES = [
    "users",
    "authentication",
    "main",
    "signatures",
]

ADDONS = [
    "channels",
    "allauth",
    "allauth.socialaccount",
    "allauth.account",
    "allauth.socialaccount.providers.github",
    "authentication.providers.google",
    "rest_framework",
    "rest_auth",
    "rest_auth.registration",
    "drf_yasg",
    "rest_framework_jwt",
    "defender",
    "dry_rest_permissions",
    "django_user_agents",
    "tracking_analyzer",
    "drf_spectacular",
    "django_prometheus",
    "rest_framework_cache",
]

INSTALLED_APPS = (
    [
        'material',
        'material.admin',
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "whitenoise.runserver_nostatic",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "contracts",
        "companymanager",
        "payroll",
        "humanresources",
        "appointments",
        "daysoff",
    ]
    + ADDONS
    + MICROSERVICES
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "defender.middleware.FailedLoginMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
]

ROOT_URLCONF = "documentmanager.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]

WSGI_APPLICATION = "documentmanager.wsgi.application"
ASGI_APPLICATION = "documentmanager.asgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "vmax_documents_new",
        "USER": "vmax_last_user",
        "PASSWORD": "Cica-slobozi-m-ai-bah!",
        "HOST": "40.113.167.20",
        "PORT": "5432",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://74.234.184.170:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

DEFENDER_REDIS_URL = "redis://74.234.184.170:6379/3"

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "none"
# AUTH_USER_MODEL = "users.User"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
AUTH_USER_MODEL = "users.User"
ACCOUNT_AUTHENTICATION_METHOD = "email"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DATE_INPUT_FORMATS": ["%d-%m-%Y"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "JWT_AUTH_COOKIE": "JWT",
    "JWT_EXPIRATION_DELTA": datetime.timedelta(minutes=6),
    "JWT_ALLOW_REFRESH": True,
    "JWT_REFRESH_EXPIRATION_DELTA": datetime.timedelta(days=7),
    "DEFAULT_SCHEMA_CLASS": "main.schema.CustomSchema",
    "SERVE_INCLUDE_SCHEMA": False,
    "TITLE": "Planner API",
    "DESCRIPTION": "Planner api used in sveltekit",
    "VERSION": "0.1.0",
}


REST_FRAMEWORK_CACHE = {
    "DEFAULT_CACHE_BACKEND": "default",
}

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "authentication.serializers.RegisterSerializer",
}

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "users.serializers.UserSerializer"
}

JWT_AUTH = {}

REST_USE_JWT = True
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = BASE_DIR / "static/"
STATIC_URL = "https://vmax-documents.vbrlabs.io/api/static/"

MEDIA_URL = "https://vmax-documents.vbrlabs.io/api/media/"
MEDIA_ROOT = BASE_DIR / "media/"

GEOIP_PATH = BASE_DIR / "geoip/"
TRACKING_ANALYZER_MAXMIND_URL = (
    "https://download.maxmind.com/app/geoip_download?edition_id="
)

TRACKING_ANALYZER_MAXMIND_CITIES = "GeoLite2-City.mmdb"
TRACKING_ANALYZER_MAXMIND_COUNTRIES = "GeoLite2-Country.mmdb"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


PROMETHEUS_METRIC_NAMESPACE = "planner"

LOG_PATH = os.path.join(BASE_DIR, "logs")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
       "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
        },
        "django.server": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}
