import os, sys, site

# enable the virtualenv
site.addsitedir('/var/www/mediamachine/mediamachine/ve/lib/python2.6/site-packages')

# paths we might need to pick up the project's settings
sys.path.append('/var/www/mediamachine/mediamachine/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mediamachine.settings_production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
