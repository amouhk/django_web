"""
Django settings for epeg project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$k$!19o_rv9vn9917$26kp)yp7&(phd6w3g-fpwu_&d=dpz!xp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'naskam',
    '82.64.149.128',
    'qnaskam.myqnapcloud.com',
    '192.168.0.10',
    '192.168.0.11'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appv',
    'appv_admin',
    # Other apps...
    'django_user_agents',
    #'feeds',# use base feed module
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # other middlewares...
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'epeg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'epeg.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    # 'epeg': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'epegobel_database',
    #     'USER': 'epegobel_user',
    #     'PASSWORD': 'AY]P~8FYbPzqP9T6a$',
    #     'HOST': '193.70.45.74',
    #     'PORT': '',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'epeg_db',
        'USER': 'django',
        'PASSWORD': 'pdU9yYvvpUgJWu3$ny*n4z8RwLm&yEd#yv9e?y@6!tM9b5JEGA629qvVNV+KAV=fr?K9jw',
        'HOST': '82.64.149.128',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_INPUT_FORMATS = ['%d-%m-%y']
# LOCALE_PATHS = (BASE_DIR + '/locale', )
DATE_FORMAT = "d-m-Y"
# USE_THOUSAND_SEPARATOR = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/share/CACHEDEV1_DATA/Web/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = '/share/Web/media/'
MEDIA_URL = '/media/'

# Cache backend is optional, but recommended to speed up user agent parsing
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'

# Sending Email
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kevin.doaho@gmail.com'
EMAIL_HOST_PASSWORD = 'kVe52OiTjG@eL+&+lE'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# For deployment
# CSRF_COOKIE_SECURE = True
#
# SECURE_SSL_REDIRECT = True
#
# SECURE_HSTS_SECONDS = 3600
#
# SECURE_HSTS_PRELOAD = True
#
# SESSION_COOKIE_SECURE = True
#
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#
# SECURE_REFERRER_POLICY = "no-referrer"

# RSS FEED
#FEEDS_USER_AGENT = "E21Feeder/1.0"
#FEEDS_SERVER = "https://evangile21.thegospelcoalition.org/dieu-qui-se-devoil/feed/"
#FEEDS_LINK_E21_DON_CARSON = "https://evangile21.thegospelcoalition.org/dieu-qui-se-devoil/feed/"

