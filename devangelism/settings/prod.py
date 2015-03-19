import os

from devangelism.settings.common import *

DEBUG = False

ADMINS = (
    ("Randall", "randhunt@amazon.com")
)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'devangelism',
        'USER': os.getenv('RDS_USER'),
        'PASSWORD': os.getenv('RDS_PASSWORD'),
        'HOST': os.getenv('RDS_HOSTNAME'),
        'PORT': os.getenv('RDS_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles/')
SECRET_KEY = os.getenv('SECRET_KEY')
