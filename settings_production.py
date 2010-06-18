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
