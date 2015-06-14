"""
Django settings for django_ianclark project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Applications
# Split up, combined at end of file into INSTALLED_APPS
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'wmd',
)

LOCAL_APPS = (
    'blog',
    'experience',
    'about',
    'tags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_ianclark.urls'

WSGI_APPLICATION = 'django_ianclark.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

SITE_ID = 1

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DEBUG = os.environ.get("DEBUG", False)
TEMPLATE_DEBUG = os.environ.get("TEMPLATE_DEBUG", False)
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "my$z5f#8qujyl(&4$b=xip9l-a*c$x$&=6jq5@@0n**oa1p&2p"
)

# Production environment can append / remove from each
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS
