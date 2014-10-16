# flake8: noqa
from settings_shared import *
import sys
import os

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

MEDIA_ROOT = '/var/www/mediamachine/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/mediamachine/mediamachine/sitemedia'),
)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'mediamachine',
        'HOST' : '',
        'PORT' : 6432,
        'USER' : '',
        'PASSWORD' : '',
        }
}

AWS_STORAGE_BUCKET_NAME = "ccnmtl-mediamachine-static-prod"
AWS_PRELOAD_METADATA = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'mediamachine.s3utils.CompressorS3BotoStorage'
S3_URL = 'https://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'https://%s.s3.amazonaws.com/compressor/' % AWS_STORAGE_BUCKET_NAME
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
DEFAULT_FILE_STORAGE = 'plexus.s3utils.MediaRootS3BotoStorage'
MEDIA_URL = S3_URL + '/media/'
COMPRESS_STORAGE = 'plexus.s3utils.CompressorS3BotoStorage'
AWS_QUERYSTRING_AUTH = False

if 'migrate' not in sys.argv:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')

try:
    from local_settings import *
except ImportError:
    pass
