from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib import databrowse
import os.path
admin.autodiscover()
import staticmedia
from mediamachine.machine.models import Video, Theme, Keyword

site_media_root = os.path.join(os.path.dirname(__file__),"media")

video_info_dict = {
    'queryset': Video.objects.all(),
}

theme_info_dict = {
    'queryset': Theme.objects.all(),
}

keyword_info_dict = {
    'queryset': Keyword.objects.all(),
}

urlpatterns = patterns('',
                       # Example:
                       # (r'^mediamachine/', include('mediamachine.foo.urls')),
                       ('^accounts/',include('djangowind.urls')),
                       ('^$','django.views.generic.simple.direct_to_template', {'template' : 'machine/index.html'}),
                       url('^video/$','django.views.generic.list_detail.object_list',
                        dict(video_info_dict,paginate_by=10, template_name='machine/video_list.html'),name='video_list'),
                       url('^video/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',
                        dict(video_info_dict,template_name='machine/video_detail.html'),name='video_detail'),


                       url('^theme/$','django.views.generic.list_detail.object_list',
                        dict(theme_info_dict,template_name='machine/theme_list.html'),name='theme_list'),
                       url('^theme/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',
                        dict(theme_info_dict,template_name='machine/theme_detail.html'),name='theme_detail'),

                       url('^keyword/$','django.views.generic.list_detail.object_list',
                        dict(keyword_info_dict,template_name='machine/keyword_list.html'),name='keyword_list'),
                       url('^keyword/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail',
                        dict(keyword_info_dict,template_name='machine/keyword_detail.html'),name='keyword_detail'),

                       (r'^databrowse/(.*)', databrowse.site.root),
                       (r'^admin/(.*)', admin.site.root),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
                       (r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

