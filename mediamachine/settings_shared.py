# Django settings for mediamachine project.
import os.path
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ( )

MANAGERS = ADMINS

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'mediamachine',
        'HOST' : '',
        'PORT' : 5432,
        'USER' : '',
        'PASSWORD' : '',
        }
}

if 'test' in sys.argv:
    DATABASES = {
        'default' : {
            'ENGINE' : 'django.db.backends.sqlite3',
            'NAME' : ':memory:',
            'HOST' : '',
            'PORT' : '',
            'USER' : '',
            'PASSWORD' : '',
            }
    }

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=mediamachine.machine',
]

SOUTH_TESTS_MIGRATE = False
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = "/var/www/mediamachine/uploads/"
MEDIA_URL = '/uploads/'
STATIC_URL = '/media/'
SECRET_KEY = ')ng#)ef_u@_^zvvu@dxm7ql-yb^_!a6%v3v^j3b(mp+)l+5%@h'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    )

MIDDLEWARE_CLASSES = (
    'django_statsd.middleware.GraphiteRequestTimingMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'mediamachine.urls'

TEMPLATE_DIRS = (
    "/var/www/mediamachine/templates/",
    os.path.join(os.path.dirname(__file__),"templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'staticmedia',
    'sorl.thumbnail',
    'django.contrib.admin',
    'tagging',
    'template_utils',
    'typogrify',
    'mediamachine.machine',
    'django.contrib.databrowse',
    'sentry.client',
    'munin',
    'django_statsd',
    'django_nose',
    'raven.contrib.django',
    'south',
    'smoketest',
)

STATSD_CLIENT = 'statsd.client'
STATSD_PREFIX = 'mediamachine'
STATSD_HOST = 'localhost'
STATSD_PORT = 8125
STATSD_PATCHES = ['django_statsd.patches.db', ]

THUMBNAIL_SUBDIR = "thumbs"
EMAIL_SUBJECT_PREFIX = "[mediamachine] "
EMAIL_HOST = 'localhost'
SERVER_EMAIL = "mediamachine@ccnmtl.columbia.edu"

# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', 'sitemedia'),
)

# WIND settings

AUTHENTICATION_BACKENDS = ('djangowind.auth.WindAuthBackend','django.contrib.auth.backends.ModelBackend',)
WIND_BASE = "https://wind.columbia.edu/"
WIND_SERVICE = "cnmtl_full_np"
WIND_PROFILE_HANDLERS = ['djangowind.auth.CDAPProfileHandler']
WIND_AFFIL_HANDLERS = ['djangowind.auth.AffilGroupMapper','djangowind.auth.StaffMapper','djangowind.auth.SuperuserMapper']
WIND_STAFF_MAPPER_GROUPS = ['tlc.cunix.local:columbia.edu']
WIND_SUPERUSER_MAPPER_GROUPS = ['anp8','jb2410','zm4','sbd12','egr2107','kmh2124','sld2131','amm8','mar227','ed2198']

# TinyMCE settings

TINYMCE_JS_URL = '/site_media/js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = 'media/js/tiny_mce'

# if you set this to True, you may have to 
# override TINYMCE_JS_ROOT with the full path on production
TINYMCE_COMPRESSOR = False 
TINYMCE_SPELLCHECKER = True

TINYMCE_DEFAULT_CONFIG = {'cols': 80, 
                          'rows': 30,
                          'plugins':'table,spellchecker,paste,searchreplace',
                          'theme' : 'simple',
                          }
