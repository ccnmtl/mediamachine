from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from django.contrib import databrowse
import os.path
admin.autodiscover()
import staticmedia
from mediamachine.machine.models import Video, Theme, Keyword
from django.contrib.auth.decorators import login_required

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
                       ('^$','machine.views.limited_direct_to_template', {'template' : 'machine/index.html'}),
                       url('^video/$','machine.views.limited_object_list',
                        dict(video_info_dict,paginate_by=10, template_name='machine/video_list.html'),name='video_list'),
                       url('^video/(?P<object_id>\d+)/$','machine.views.limited_object_detail',
                        dict(video_info_dict,template_name='machine/video_detail.html'),name='video_detail'),


                       url('^theme/$','machine.views.limited_object_list',
                        dict(theme_info_dict,template_name='machine/theme_list.html'),name='theme_list'),
                       url('^theme/(?P<object_id>\d+)/$','machine.views.limited_object_detail',
                        dict(theme_info_dict,template_name='machine/theme_detail.html'),name='theme_detail'),

                       url('^keyword/$','machine.views.limited_object_list',
                        dict(keyword_info_dict,template_name='machine/keyword_list.html'),name='keyword_list'),
                       url('^keyword/(?P<object_id>\d+)/$','machine.views.limited_object_detail',
                        dict(keyword_info_dict,template_name='machine/keyword_detail.html'),name='keyword_detail'),

                       (r'^databrowse/(.*)', login_required(databrowse.site.root)),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^munin/',include('munin.urls')),
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media_root}),
                       (r'^uploads/(?P<path>.*)$','django.views.static.serve',{'document_root' : settings.MEDIA_ROOT}),
) + staticmedia.serve()

