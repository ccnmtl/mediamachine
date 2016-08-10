import django_databrowse
import django.views.static

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from mediamachine.machine.models import Video, Theme, Keyword
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
admin.autodiscover()


urlpatterns = [
    url('^accounts/', include('djangowind.urls')),
    url('^$', login_required(
        TemplateView.as_view(
            template_name="machine/index.html"))),
    url('^video/$',
        login_required(
            ListView.as_view(
                queryset=Video.objects.all(),
                template_name="machine/video_list.html",
                paginate_by=10,
            )
        ), name='video_list'),

    url('^video/(?P<pk>\d+)/$',
        login_required(
            DetailView.as_view(
                model=Video,
                template_name='machine/video_detail.html',
            )
        ),
        name='video_detail'),

    url('^theme/$',
        login_required(
            ListView.as_view(
                queryset=Theme.objects.all(),
                template_name="machine/theme_list.html",
            )
        ),
        name='theme_list'),
    url('^theme/(?P<pk>\d+)/$',
        login_required(
            DetailView.as_view(
                model=Theme,
                template_name="machine/theme_detail.html",
            )
        ),
        name='theme_detail'),

    url('^keyword/$',
        login_required(
            ListView.as_view(
                queryset=Keyword.objects.all(),
                template_name="machine/keyword_list.html",
            )
        ),
        name='keyword_list'),
    url('^keyword/(?P<pk>\d+)/$',
        login_required(
            DetailView.as_view(
                model=Keyword,
                template_name="machine/keyword_detail.html",
            )
        ),
        name='keyword_detail'),

    url(r'^databrowse/(.*)', login_required(django_databrowse.site.root)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stats/$', TemplateView.as_view(template_name="stats.html")),
    url(r'^smoketest/', include('smoketest.urls')),
    url(r'^uploads/(?P<path>.*)$',
        django.views.static.serve,
        {'document_root': settings.MEDIA_ROOT}),
]
