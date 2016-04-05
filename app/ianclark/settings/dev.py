from ianclark.settings.base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ianclark',
        'USER': 'ian',
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = True
