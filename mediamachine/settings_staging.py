# flake8: noqa
from settings_shared import *
import sys

TEMPLATE_DIRS = (
    "/var/www/mediamachine/mediamachine/mediamachine/templates",
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

SENTRY_SITE = 'mediamachine-staging'
SENTRY_SERVERS = ['http://sentry.ccnmtl.columbia.edu/sentry/store/']

if 'migrate' not in sys.argv:
    import logging
    from raven.contrib.django.handlers import SentryHandler
    logger = logging.getLogger()
    # ensure we havent already registered the handler
    if SentryHandler not in map(type, logger.handlers):
        logger.addHandler(SentryHandler())

        # Add StreamHandler to sentry's default so you can catch missed exceptions
        logger = logging.getLogger('sentry.errors')
        logger.propagate = False
        logger.addHandler(logging.StreamHandler())

try:
    from local_settings import *
except ImportError:
    pass
