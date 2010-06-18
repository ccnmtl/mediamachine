from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib import databrowse
import os.path
admin.autodiscover()
import staticmedia

site_media_root = os.path.join(os.path.dirname(__file__),"media")

urlpatterns = patterns('',
                       # Example:
                       # (r'^mediamachine/', include('mediamachine.foo.urls')),
                       ('^accounts/',include('djangowind.urls')),
                       ('^$','django.views.generic.simple.redirect_to', {'url': '/databrowse/'}),
                       (r'^databrowse/(.*)', databrowse.site.root),
                       (r'^admin/(.*)', admin.site.root),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
                       (r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

