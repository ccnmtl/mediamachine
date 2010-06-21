from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib import databrowse
import os.path
admin.autodiscover()
import staticmedia
from mediamachine.machine.models import Video

site_media_root = os.path.join(os.path.dirname(__file__),"media")

video_info_dict = {
    'queryset': Video.objects.all(),
}

urlpatterns = patterns('',
                       # Example:
                       # (r'^mediamachine/', include('mediamachine.foo.urls')),
                       ('^accounts/',include('djangowind.urls')),
                       ('^$','django.views.generic.simple.redirect_to', {'url': '/databrowse/'}),
                       url('^video/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',
                        dict(video_info_dict,template_name='machine/video_detail.html'),name='video_detail'),
                       (r'^databrowse/(.*)', databrowse.site.root),
                       (r'^admin/(.*)', admin.site.root),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
                       (r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

