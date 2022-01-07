"""
Django settings for Maktab_52_Django_Clothing_Store project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from logging import LogRecord
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from jedi.plugins import *
from jedi.plugins import django

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dw6ztv7%%h_w0zq2m-^ljbe2@6@417p56x457kcr+gxbye6(w-'
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',

    'jalali_date',
    'captcha',

    'core',
    'landing',
    'order',
    'product',
    'customer',
    'contact',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'core.middleware.TimingMiddleware'
]

ROOT_URLCONF = 'Maktab_52_Django_Clothing_Store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Maktab_52_Django_Clothing_Store.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'dev': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    'production': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '1234567890',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

DATABASES['default'] = DATABASES['dev' if DEBUG else 'production']

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOCALE_PATHS = [BASE_DIR / "locale"]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_URL = 'customer:login'
LOGIN_REDIRECT_URL = 'customer:profile_detail'

AUTH_USER_MODEL = 'customer.User'

# CONTACT_EMAIL = 'mohammad.h.tabatabaei78@gmail.com'
# ADMIN_EMAILS = ['admin@example.com', ]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mohammad.h.tabatabaei78@gmail.com'
EMAIL_HOST_PASSWORD = 'hsjaupzimcnufych'


CAPTCHA_FONT_SIZE = 30
CAPTCHA_LETTER_ROTATION = (-20, 20)


def length_limit(record: LogRecord) -> bool:
    if int(len(record.getMessage())) > 20:
        return True
    return False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'short': {
            'format': "{levelname} {asctime}: '{message}'",
            'style': '{'
        },
        'verbose': {
            'format': "{levelname} {asctime}: '{message}' at {module} (process: {process}, thread: {thread})",
            'style': '{'
        },
    },

    'filters': {
        'length_limit': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': length_limit,
        }
    },

    'handlers': {
        'my-console': {
            'class': 'logging.StreamHandler',
            'formatter': 'short'
        },
        'my-file-project': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'log/project.log',
            'formatter': 'verbose',
            'level': 'ERROR'
        },
        'my-file-developers': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'log/developers.log',
            'formatter': 'verbose',
            'level': 'ERROR'
        },
    },

    'root': {
        'handlers': ['my-console'],
        'level': 'DEBUG',
        'filters': ['length_limit']
    },

    'loggers': {
        'timing': {
            'handlers': ['my-console'],
            'level': 'INFO',
            'propagate': False,
        },
        'project': {
            'handlers': ['my-file-project'],
            'level': 'ERROR',
            'propagate': True,
        },
        'project.developers': {
            'handlers': ['my-file-developers'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
