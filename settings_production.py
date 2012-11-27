from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/mediamachine/mediamachine/templates",
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

try:
    from local_settings import *
except ImportError:
    pass
